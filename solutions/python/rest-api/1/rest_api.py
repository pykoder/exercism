import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users':
            if payload:
                data = json.loads(payload)
                users = data.get('users',[])
                result = []
                for user in users:
                    for record in self.database.get('users',[]):
                        if record.get('name') == user:
                            result.append(record)
                return json.dumps({'users': result})
        return json.dumps({"users": []})

    def post(self, url, payload=None):
        if url == '/add':
            if payload:
                data = json.loads(payload)
                if 'user' in data:
                    record = {"name": data.get('user','nemo'), "owes": {}, "owed_by": {}, "balance": 0.0}
                self.database['users'].append(record)
                return json.dumps(record)
        if url == '/iou':
            if payload:
                data = json.loads(payload)
                lender = data.get("lender")
                borrower = data.get("borrower")
                amount = data.get("amount")

                lender_record = {}
                borrower_record = {}
                for record in self.database.get('users'):
                    if record.get("name") == lender:
                        lender_record = record
                        record["balance"] += amount
                        owed_by = record.get('owed_by')
                        owed_by[borrower] = owed_by.get(borrower,0.0) + amount
                    if record.get("name") == borrower:
                        borrower_record = record
                        record["balance"] -= amount
                        owes = record.get('owes')
                        owes[lender] = owes.get(lender,0.0) + amount
                if not lender_record:
                    lender_record = {"name": lender, "owes": {}, "owed_by": {borrower: amount}, "balance": amount}
                    self.database["users"].append(lender_record)
                if not borrower_record:
                    borrower_record = {"name": borrower, "owes": {lender: amount}, "owed_by": {}, "balance": -amount}
                    self.database["users"].append(borrower_record)
                for record in [borrower_record, lender_record]:
                    for name in list(record.get("owes").keys()):
                        if name in record.get("owed_by") and name in record.get("owes"):
                            owes = record.get("owes")[name]
                            owed_by = record.get("owed_by")[name]
                            if owes == owed_by:
                                del record["owed_by"][name]
                                del record["owes"][name]
                            elif owes > owed_by:
                                del record["owed_by"][name]
                                record["owes"][name]=owes-owed_by
                            else:
                                del record["owes"][name]
                                record["owed_by"][name]=owed_by-owes
                if lender_record.get('name') < borrower_record.get('name'):
                    summary = {'users': [lender_record, borrower_record]}
                else:
                    summary = {'users': [borrower_record, lender_record]}
                return json.dumps(summary)
