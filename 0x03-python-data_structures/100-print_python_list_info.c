#include <stdlib.h>
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about a python list
 *
 * @p: PyObject pointer to the python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	size = PyList_Size(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
