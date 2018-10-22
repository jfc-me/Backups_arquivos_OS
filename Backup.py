import os
import zipfile

class Backup:

    def compactarTudo(self, caminho):

        caminho = os.path.abspath(caminho)
        ver = 'dir ' + caminho
        os.system(ver)
        var = 1
        print("="*70)
        while True:
            compactar = os.path.basename(caminho) + '_' + str(var) + '.zip'
            if not os.path.exists(compactar):
                print(':==> Sem Paridade')
                break
            var += 1
        print('Compactado  :==> ', compactar)
        backupZip = zipfile.ZipFile(compactar, 'w')
        for pastaN, spasta, arqv in os.walk(caminho):
            print('Add :==> ', pastaN)
            backupZip.write(pastaN)
            for filename in arqv:
                if filename.startswith(os.path.basename(caminho) + '_') and filename.endswith('.zip'):
                    continue
                backupZip.write(os.path.join(pastaN, filename))
        backupZip.close()
        print("Isso Fica contente e feliz.")


Backup().compactarTudo("/")

