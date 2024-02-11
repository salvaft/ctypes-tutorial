#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int sum_array(int *arr, int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}

// Bitwise copying the array from one stack to another
typedef struct
{
    int my_array[5];
} ArrayOfFive;

ArrayOfFive new_array()
{
    ArrayOfFive container = {{0, 0, 0, 0, 0}};

    return container;
}

int *increment_array(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        arr[i] = arr[i] + 1;
    };
    return arr;
}