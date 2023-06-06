#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *next, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;
	if (current == NULL)
	{
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->n > number)
		{
			next = current;
			new->next = current;
			*head = new;
			return (new);
		}
		else if (current->next != NULL)
		{
			if (current->next->n > number)
			{
				next = current->next;
				current->next = new;
				new->next = next;
				return (new);
			}
			current = current->next;
		}
		else
		{
			current->next = new;
			return (new);
		}
	}
}
