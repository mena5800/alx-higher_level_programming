#include "lists.h"

/**
 * check_cycle - check if the linked list is cycle or not
 * @list: the linked list
 * Return: 0 if no cycle - 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;

	while (list->next)
	{
		if (list->next == first)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
