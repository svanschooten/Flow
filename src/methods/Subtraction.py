from methods.AbstactMethod import AbstractMethod


class Subtraction(AbstractMethod):
    name = 'Subtraction'

    def apply(self, args: dict) -> dict:
        return {
            'res': args.get('x') - args.get('y')
        }
