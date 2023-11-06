#include "lists.h"


listint_t *rev_list(listint_t **head);
/**
 *  * is_palindrome - checks if a list is a palindrome
 *   * @head: pointer to a linked list
 *    * Return: Always 0 Success.
 *     */
int is_palindrome(listint_t **head)
{
		listint_t *slow = *head, *fast = *head,*f_half, *sec_half;
			listint_t *prev = NULL, *next = NULL;
				listint_t *mid = NULL;
					int flag = 1;

						if (*head == NULL || (*head)->next == NULL)
									return (1);

							while (fast != NULL && fast->next != NULL)
									{
												fast = fast->next->next;
														prev = slow;
																slow = slow->next;
																	}

								if (fast != NULL)
										{
													mid = slow;
															slow = slow->next;
																}

									next = slow;
										prev->next = NULL;

											mid = (mid == NULL) ? rev_list(&next) : mid;

												f_half = *head;
													sec_half = mid;

														while (f_half != NULL && sec_half != NULL)
																{
																			if (f_half->n != sec_half->n)
																						{
																										flag = 0;
																													break;
																															}
																					f_half = f_half->next;
																							sec_half = sec_half->next;
																								}

															/* restore the orig list */
															rev_list(&mid);
																rev_list(head);

																	return (flag);
}
/**
 *  * rev_list - reverses a linked list
 *   * @head: pointer to a node
 *    * Return: pointer to the head node
 *     */
listint_t *rev_list(listint_t **head)
{
		listint_t *prev = NULL;
			listint_t *current = *head;
				listint_t *next = NULL;

					while (current != NULL)
							{
										next = current->next;
												current->next = prev;
														prev = current;
																current = next;
																	}
						*head = prev;

							return (*head);
}


