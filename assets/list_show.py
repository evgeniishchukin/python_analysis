class ListShow:
    '''Show list of data in the normal view'''

    def __init__(self):
        pass

    def show(self, list_to_show):
        print('\n\n')
        for i, value in enumerate(list_to_show):
            print(f'#{i+1}: {value}')


list_show = ListShow()
