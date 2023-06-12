#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *new = *head;
	int flag = 1, i, j, new_counter = 0, counter = 0;

	if (current == NULL || current->next == NULL)
	{
		return (1);
	}
	while (current)
	{
		counter++;
		current = current->next;
	}
	current = *head;
	flag = 1;
	new_counter = counter - 1;
	for (i = 0; i < counter / 2; i++)
	{
		for (j = 0; j < new_counter; j++)
		{
			new = new->next;
		}
		new_counter -= 2;
		if (current->n != new->n)
		{
			flag = 0;
			break;
		}
		current = current->next;
		new = current;
	}

	return (flag);
}
