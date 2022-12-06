#include <stdio.h>
#include <python.h>

/**
* prints some basic info about Python lists
*
*
*/
void print_python_list_info(PyObject *p)
{
    long int size, i;
    pyListObject *list;
    pyObject *obj;

    size = py_SIZE(p);
    printf("[*] size of the python List = %ld\n", size);

    list = (pyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = pyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, py_TYPE(obj)->tp_name;
    }
}
