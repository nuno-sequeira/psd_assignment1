from pyrsistent import s


def get_relation_class(members, relation):

    class Relation:
        def __init__(self):
            if not relation:
                self.relation = s()
            else:
                self.relation = relation
            self.members = members

        def __iter__(self):
            return self.members.__iter__()

        def contains(self, el):
            """does the relation contain given element"""
            return el in self.relation

        def add(self, el):
            """adding an element to the relation"""
            return get_relation_class(self.members, self.relation.add(el))

        def remove(self, el):
            """removing an element from the relation"""
            if el in self.relation:
                return get_relation_class(self.members, self.relation.remove(el))

        def union(self, other):
            """union of two relations"""
            return get_relation_class(self.members, self.relation.union(other.relation))

        def intersection(self, other):
            """intersection of two relations"""
            return get_relation_class(self.members, self.relation.intersection(other.relation))

        def subtraction(self, other):
            """subtraction of two relations"""
            return get_relation_class(self.members, self.relation.difference(other.relation))

        def inverse_rel(self):
            """inverse relation"""
            temp = s()
            for x, y in self.relation:
                temp = temp.add((y, x))
            return get_relation_class(self.members, temp)

        def reflexive(self):
            """is the relation reflexive"""
            for x in self.members:
                if (x, x) not in self.relation:
                    return False
            return True

        def symmetric(self):
            """is the relation symmetric"""
            for (x, y) in self.relation:
                if (y, x) not in self.relation:
                    return False
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

            return get_relation_class(self.members, relation)

        def prt(self):
            print(self.relation)

    return Relation()


"""
rel = get_relation_class(s(1, 2, 3, 4), None)
rel.prt()
print("c", rel.contains(("one", "two")))
rel2 = rel.add(("one", "two"))
rel3 = rel2.add(("three", "four"))
rel4 = rel3.add(("one", "four"))
rel4.prt()
rel5 = rel4.remove(("one", "two"))
rel5.prt()
relOther = get_relation_class(s(), None)
relOther1 = relOther.add(("one", "two"))
relOther2 = relOther1.add(("oned", "twod"))
relOther3 = relOther2.add(("onedes", "twodes"))
relOther3.prt()
rel6 = rel5.union(relOther3)
rel6.prt()
rel7 = rel6.intersection(relOther3)
rel7.prt()
relOtherX = get_relation_class(s(), None)
relOtherX1 = relOtherX.add(("one", "two"))
relOtherX2 = rel7.subtraction(relOtherX1)
relOtherX2.prt()
rel8 = relOtherX2.inverse_rel()
rel8.prt()
relX = get_relation_class(s(1, 2, 3), s((1, 2), (2, 3), (2, 1)))
print(rel.reflexive())
print(relX.symmetric())
print(rel.transitive())
rel9 = get_relation_class(s(1, 2, 3, 4), s((1, 2), (2, 3), (3, 4)))
rel9.prt()
rel10 = rel9.reflexive_transitive()
rel10.prt()
"""