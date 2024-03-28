a, b, c = map(int, input('3개 복권번호: ').split())
if a==2:
        if b==3 and c==9:
            print('상금 1억 원')
        elif b==3 or c==9:
            print('상금 1천만 원')
        elif b!=3 or c!=9:
            print('상금 1만 원')
        else:
                print('다음 기회에...')
elif b==3:
        if a==2 and c==9:
            print('상금 1억 원')
        elif a==2 or c==9:
            print('상금 1천만 원')
        elif a!=2 or c!=9:
            print('상금 1만 원')
        else:
            print('다음 기회에...')
elif c==9:
        if b==3 and a==2:
            print('상금 1억 원')
        elif b==3 or a==2:
            print('상금 1천만 원')
        elif b!=3 or a!=2:
            print('상금 1만 원')
        else:
            print('다음 기회에...')
else:
            print('다음 기회에...')
