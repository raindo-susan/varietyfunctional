import numpy as np
from pyscf import gto, scf, mcscf, fci, ao2mo


mol=gto.M(atom="0 0 0 0; 0 0 0 1.2", basis={"O": "cc-pVDZ","H": "cc-pVTZ"})
mf=scf.RHF(mol)
mf.kernel()

mo_energy = mf.mo_energy



print(mo_energy)
