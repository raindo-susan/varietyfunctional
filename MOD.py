from pysmiles import read_smiles

#smiles = 'O'
#mol = read_smiles(smiles)
#mol = gto.Mole()
#mol.atom = [f'{atom[0]} {atom[1][0]} {atom[1][1]} {atom[1][2]}' for atom in mol.atoms]
#mol.build()
#mol.basis = 'sto-3g'
from pyscf import gto, scf
b='STO-3G'
mol = gto.M(atom='O 0 0 0; O 0 0 1.2', basis=b)
mf = scf.RHF(mol)
mf.kernel()

mo_energy = mf.mo_energy
print(type(mo_energy))
print(mo_energy)

# Add energy levels to the diagram
#for i in enumerate(mo_energy):
   # if i == np.floor(mf.nelec[0]/2):
    #    print(i)
