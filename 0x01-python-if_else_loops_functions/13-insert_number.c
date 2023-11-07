#include "lists.h"
#include <stdlib.h>

/**
 * is_sorted - checks if a list is sorted in ascending or descending order
 *
 * @head: pointer to a linked list
 *
 * Return: 0 if ascending, 1 if descending, -1 if unsorted
 */
int is_sorted(listint_t *head)
{
	int ascending = 0, descending = 0;
	listint_t *current = head;

	if (head == NULL || head->next == NULL)
		return (-1);

	while (current->next != NULL)
	{
		if (current->n < current->next->n)
			ascending = 1;
		else if (current->n > current->next->n)
			descending = 1;
		if (ascending && descending)
			return (-1);
		current = current->next;
	}
	if (ascending)
		return (0);
	if (descending)
		return (1);

	return (-1);
}


/**
 * insert_node - A function that inserts a number into a sorted singly linked
 * list
 *
 * @head: a pointer to the head of the list.
 * @number: the number to be inserted.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *temp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (current == NULL)
	{
		new->n = number;
		*head = new;
		return (new);
	}
	else
	{
		if (is_sorted(*head) == 0)
		{
			if (current->n >= number)
			{
				new->n = number;
				new->next = current;
				*head = new;
			}
			else
			{
				while (current->next->n < number)
					current = current->next;
				temp = current->next;
				new->n = number;
				new->next = temp;
				current->next = new;
			}
		}
		else if (is_sorted(*head) == 1)
		{
			if (current->n <= number)
			{
				new->n = number;
				new->next = current;
				*head = new;
			}
			else
			{
				while (current->next->n > number)
					current = current->next;
				temp = current->next;
				new->n = number;
				new->next = temp;
				current->next = new;
			}
		}
	}
	return (new);
}
