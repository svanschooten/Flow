from methods.AbstactMethod import AbstractMethod


class Addition(AbstractMethod):
    name = 'Addition'

    def apply(self, args: dict) -> dict:
        return {
            'res': args.get('x') + args.get('y')
        }
