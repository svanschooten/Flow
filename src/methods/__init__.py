from methods.AbstactMethod import AbstractMethod
from methods.Addition import Addition
from methods.Subtraction import Subtraction

methods = {
    AbstractMethod.name: AbstractMethod,
    Addition.name: Addition,
    Subtraction.name: Subtraction
}