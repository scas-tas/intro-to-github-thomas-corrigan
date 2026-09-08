"""
BEGIN BubbleSort(numbers, size)
	FOR i = 0 TO size - 2
    	FOR j = 0 TO size - 2 - i
        	IF numbers[j] > numbers[j + 1] THEN
            	temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
        	ENDIF
    	NEXT j
	NEXT i
END BubbleSort
"""


def bubblesort(number, size):
    