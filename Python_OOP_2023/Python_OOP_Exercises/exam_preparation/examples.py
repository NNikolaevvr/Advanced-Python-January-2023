#next filter example
from calendar import month_name


def rent_dvd(self, customer_id, dvd_id):
    customer = next(filter(lambda x: x.id == customer_id, self.customers))
    dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))


#example of class method
#@classmethod
def from_date(cls,id,name,date, age_restriction):
    day, month, year = [int(x) for x in date.split(".")]
    return cls(name, id, year, month_name[month], age_restriction)


def __repr__(self):              # unpacking nested list
    return "\n".join([
    *[str(c) for c in self.customers],
    *[str(d) for d in self.dvds]])