#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct
{
    int x;
    int y;
} Point;

void print_point(Point p)
{
    printf("print_point Point: (%d, %d)\n", p.x, p.y);
}

Point create_point(int x, int y)
{
    Point p = {};
    p.x = x;
    p.y = y;
    return p;
}

Point *create_point_pointer(int a, int b)
{
    Point *p = (Point *)malloc(sizeof(Point));
    if (p != NULL)
    {
        p->x = a;
        p->y = b;
    }
    return p;
}

void free_point(Point *p)
{
    free(p);
}

typedef struct
{
    Point *points;
    int size;
} PointArray;

PointArray create_point_array(int size)
{

    PointArray array;
    array.points = malloc(size * sizeof(Point));
    array.size = size;
    for (int i = 0; i < size; i++)
    {
        array.points[i].x = 2;
        array.points[i].y = 3;
    }
    return array;
}

void free_point_array(PointArray array)
{
    free(array.points);
}