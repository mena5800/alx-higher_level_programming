#include "lists.h"

/**
 * check_cycle - check if the linked list is cycle or not
 * @list: the linked list
 * Return: 0 if no cycle - 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	while (first != NULL && second->next != NULL &&
		   second->next->next != NULL)
	{
		if (second == first)
		{
			return (1);
		}
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
