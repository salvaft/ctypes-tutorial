#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *fullName(char *firstName, char *lastName)
{
    char *fullName = malloc(strlen(firstName) + strlen(lastName) + 1);
    strcpy(fullName, firstName);
    strcat(fullName, " ");
    strcat(fullName, lastName);
    return fullName;
}
