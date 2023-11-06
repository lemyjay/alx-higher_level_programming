#include "lists.h"
#include <stdlib.h>


/**
 * is_palindrome - A function that checks if a singly linked list is a
 * palindrome. An empty list is considered a palindrome.
 *
 * @head: a pointer to the the head of the list.
 *
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int len = 0, ret = 1, a = 0, i, /*number,*/number[10240];
	listint_t *current = *head;

	if (current == NULL)
		return (1);
	while (current != NULL)
	{
		current = current->next;
		len++;
	}

	/*number = malloc(sizeof(int) * len);*/
	current = *head;
	while (current != NULL)
	{
		number[a] = current->n;
		current = current->next;
		a++;
	}

	for (i = 0; i < (len / 2); i++)
	{
		if (number[i] != number[a - 1])
		{
			ret = 0;
			break;
		}
		a--;
	}

	/*free(number);*/
	return (ret);
}
