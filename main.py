with open('1.txt', 'r', encoding='utf-8') as firstFile:
    with open('2.txt', 'r', encoding='utf-8') as secondFile:
        with open('3.txt', 'r', encoding='utf-8') as thirdFile:
            dictFile = {
                firstFile.name: firstFile.readlines(),
                secondFile.name: secondFile.readlines(),
                thirdFile.name: thirdFile.readlines()
            }
            dictFile = {k: v for k, v in sorted(dictFile.items(), key=lambda item: item[1], reverse=True)}
            newFile = open('newFile.txt', 'w', encoding='utf-8')
            for key, value in dictFile.items():
                newFile.write(f'{key}\n')
                newFile.write(f'{len(value)}\n')
                for line in value:
                    newFile.write(f'{line.strip()}\n')
            newFile.close()

