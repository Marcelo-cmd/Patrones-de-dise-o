"""
Memento pattern example.
"""


class Androide(object):
    def __init__(self, forma):
        self._forma = forma

    def get_saved_forma(self):
        return self._forma


class CellFormaUno(object):
    _forma = "Uno"

    def set(self, forma):
        print("CellFormaUno: Setting state to", forma)
        self._forma = forma

    def save_to_androide(self):
        print("CellFormaUno: Saving to Androide.")
        return Androide(self._forma)

    def restore_from_androide(self, androide):
        self._forma = androide.get_saved_forma()
        print("CellFormaUno: State after restoring from Androide:", self._forma)


saved_formas = []
cellformauno = CellFormaUno()
cellformauno.set("Forma Uno")
cellformauno.set("forma semi-perfacta")
saved_formas.append(cellformauno.save_to_androide())

cellformauno.set("forma perfecta")
saved_formas.append(cellformauno.save_to_androide())

cellformauno.set("forma super-perfecta")

cellformauno.restore_from_androide(saved_formas[0])
