#include "lists.h"
/**
 * insert_node - insert a new node in the list specify by head
 * @head: list where we must add
 * @number: node to add
 *
 * Return: the address of the new node
 * Null otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *tmp;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (number < (*head)->n)
	{
		new->next = *head;
		head = &new;
		return (new);
	}
	tmp = *head;
	while (tmp != NULL)
	{
		if (tmp->next->n > number)
		{
			new->next = tmp->next;
			tmp->next = new;
			break;
		}
		else
		{
			if (tmp->next == NULL)
			{
				tmp->next = new;
				new->next = NULL;
				return (new);
			}
			else
				tmp = tmp->next;
		}
	}
	return (new);
}
