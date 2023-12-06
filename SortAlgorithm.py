class SortAlgorithm:
    @classmethod
    def insertionSort(self, nums):

        # Выдаем ошибку, если список nums пуст
        if not nums:
            raise Exception("Список nums пуст")

        # Выдаем ошибку, если nums не список
        if not isinstance(nums, list):
            raise TypeError("Неверный тип, nums должен быть списком")

        # Копируем список, чтоб не менять переданный аргумент nums
        numsCopy = nums.copy()

        # Число элементов в списке
        numsCopyCount = len(numsCopy)

        # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
        for i in range(1, numsCopyCount):
            for j in range(i, 0, -1):

                if not isinstance(numsCopy[j], int):
                    raise TypeError("Неверный тип элемента '%s', в списке должны быть только числа" % (numsCopy[j]))

                if not isinstance(numsCopy[j - 1], int):
                    raise TypeError("Неверный тип элемента '%s', в списке должны быть только числа" % (numsCopy[j - 1]))

                # Если число меньше, чем предыдущее, то меняем местами и переходим к следующему числу
                if numsCopy[j] < numsCopy[j - 1]:
                    numsCopy[j], numsCopy[j - 1] = numsCopy[j - 1], numsCopy[j]
                # Если число больше, чем предыдущее, то оно уже находится на нужном месте, переходим к следующему числу
                else:
                    break
        return numsCopy