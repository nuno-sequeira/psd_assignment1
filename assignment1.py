from pyrsistent import s


def get_relation_class(a):

    class Relation:
        def __init__(self):
            self.relation = s()
            self.members = a

        def __iter__(self):
            return self.members.__iter__()

        def contains(self, el):
            """does the relation contain given element"""
            return el in self.relation

        def add(self, el):
            """adding an element to the relation"""
            self.relation = self.relation.add(el)

        def remove(self, el):
            """removing an element from the relation"""
            if el in self.relation:
                self.relation = self.relation.remove(el)

        def union(self, other):
            """union of two relations"""
            self.relation = self.relation.union(other.relation)

        def intersection(self, other):
            """intersection of two relations"""
            self.relation = self.relation.intersection(other.relation)

        def subtraction(self, other):
            """subtraction of two relations"""
            self.relation = self.relation.difference(other.relation)

        def inverse_rel(self):
            """inverse relation"""
            temp = s()
            for x, y in self.relation:
                temp = temp.add((y, x))
            self.relation = temp

        def reflexive(self):
            """is the relation reflexive"""
            for x in self.members:
                if (x, x) not in self.relation:
                    return False
            return True

        def symmetric(self):
            """is the relation symmetric"""
            temp = []
            for (x, y) in self.relation:
                if (x, y) not in temp:
                    if (y, x) not in self.relation:
                        return False
                temp.append((x, y))
                temp.append((y, x))
            return True

        def transitive(self):
            """is the relation transitive"""
            for (x, y) in self.relation:
                for (w, v) in self.relation:
                    if y == w and ((x, v) not in self.relation):
                        return False
            return True

        def reflexive_transitive(self):
            """reflexive-transitive closure"""
            relation = self.relation
            temp = s()
            for x in self.members:
                if (x, x) not in self.relation:
                    temp = temp.add((x, x))
            while True:
                for x, y in relation:
                    for w, v in relation:
                        if w == y:
                            temp = temp.add((x, v))
                current = relation.union(temp)
                if current == relation:
                    break
                relation = current

            return relation

        def prt(self):
            print(self.relation)

    return Relation()


"""
rel = get_relation_class(s(1, 2, 3, 4))
rel.prt()
print("c", rel.contains(("one", "two")))
rel.add(("one", "two"))
rel.add(("three", "four"))
rel.add(("one", "four"))
rel.prt()
#rel.remove(("oned", "twod"))
rel.prt()
relOther = get_relation_class(s())
relOther.add(("one", "two"))
relOther.add(("oned", "twod"))
relOther.add(("onedes", "twodes"))
#rel.union(relOther)
rel.prt()
#rel.intersection(relOther)
rel.prt()
relOtherX = get_relation_class(s())
relOtherX.add(("one", "two"))
#rel.subtraction(relOtherX)
rel.prt()
#rel.inverse_rel()
rel.prt()
print(rel.reflexive())
print(rel.symmetric())
print(rel.transitive())
print(rel.reflexive_transitive())
"""
