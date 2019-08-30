from AbstactMethod import AbstractMethod


class Subtraction(AbstractMethod):
    name = 'Subtraction'

    def apply(self, args):
        return {
            'res': args.get('x') - args.get('y')
        }
