#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list - Prints information about python lists
 * 
 * @p: PyObject representing a python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else if (PyList_Check(obj))
			print_python_list(obj);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes
 *
 * @p: PyObject representing Python bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n  trying string: %s\n", size, str ? str : "");
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints information about Python floats
 *
 * @p: PyObject representing a python float
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
