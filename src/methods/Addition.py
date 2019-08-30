from AbstactMethod import AbstractMethod


class Addition(AbstractMethod):
    name = 'Addition'

    def apply(self, args):
        return {
            'res': args.get('x') + args.get('y')
        }
