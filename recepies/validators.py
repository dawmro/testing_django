from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError




def validate_unit_of_measure(value):
    # create instance of unit registry
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{e}")
    except:
        raise ValidationError(f"{value} is not a valid unit of measurement")
        