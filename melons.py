"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Base Class for Domestic and International Melon Orders"""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.christmas = False

    def is_christmas(self):
        """Sets christmas to true."""

        self.christmas = True        

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_total(self):
        """Calculate price."""

        base_price = 5
        christmas_base_price = (base_price * 1.5)

        if christmas == True:
            total = (1 + self.tax) * self.qty * christmas_base_price
            return total

        else:
            total = (1 + self.tax) * self.qty * base_price
            return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

