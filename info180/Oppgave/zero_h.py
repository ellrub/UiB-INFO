from heuristic import Heuristic


class ZeroH(Heuristic):

    @staticmethod
    def h(node):
        return 0
    
class FirstHeuristic(Heuristic):
    
    @staticmethod
    def h(node):
        x = node.i
        y = node.j

        return abs(x - y)

class SecondHeuristic(Heuristic):

    @staticmethod
    def h(node):
        