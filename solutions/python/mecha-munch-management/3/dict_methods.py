"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for item, recipe in recipe_updates:
        ideas[item] = recipe
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.

    Note: this is a really silly function since dictionaries are
    inherently unordered in versions of Python prior to 3.7,
    and from 3.7 onwards they maintain insertion order, 
    not alphabetical order of keys.
    Why is it silly: because dictionnaries are designed to provide
    fast access or update of values via keys (O(1) or near O(1)).
    This sorting requirements implies rewriting the entire dictionnary.
    Thanks god, it's only the shopping cart and not the entire store inventory!
    """
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.

    """
    fulfillment = {}
    for item, qty in cart.items():
        aisle, refrigeration = aisle_mapping.get(item, ['Unknown', False])
        fulfillment[item] = [qty, aisle, refrigeration]
    #TODO: The test cases for this function are broken by design,
    # The result dictionnary is expected to be sorted in reverse alphabetical order,
    # see note in sort_entries function above. This is a really bad requirement.
    # To make it work we have to insert the keys in the dictionnary in reverse alphabetical order.
    # We could do that in the for loop above using reverse, but I prefer 
    # makeing the silly sorting explicit here.
    # The actual fix would be to remove that dummy requirement from the tests,
    # just remove the OrderedDict comparison in the test function test_send_to_store
    return dict(sorted(fulfillment.items(), reverse = True))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.

    Note: using the string "Out of stock" to indicate no remaining stock
    seems an utterly bizarre design choice, but it's in the tests so...

    If the cart contains an item not in the store inventory,
    we should raise an error rather than assuming a default value.
    But the tests don't care about that, so we don't care...
    """
    for item, (qty, _, _) in fulfillment_cart.items():
        store_qty, _, _ = store_inventory.get(item, [0, "Unknown" , False])
        remaining = int(store_qty) - qty if store_qty > qty else "Out of Stock"
        store_inventory[item][0] = remaining
    return store_inventory

