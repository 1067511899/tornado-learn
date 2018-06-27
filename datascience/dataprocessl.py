with open('dlzb.txt', encoding='UTF-8') as f:
    with open('dlzbnew.txt', 'w', encoding='UTF-8') as f1:
        ss = f.read().split(',')
        count = 1
        for x in ss:
            if count % 3 != 0:
                f1.write(x.strip() + ',')
            else:
                f1.write(x.strip() + '\n')
            count += 1

