def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

hasil = hitung_pangkat(3, 3)
print(f'Hasil = {hasil}')