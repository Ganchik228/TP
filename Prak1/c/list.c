#include "list.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

list_t *list_create(size_t data_size) {
    list_t *list = malloc(sizeof(list_t));
    if (!list) return NULL;
    
    list->head = NULL;
    list->data_size = data_size;
    return list;
}

void list_destroy(list_t *list) {
    if (!list) return;
    
    list_node_t *current = list->head;
    while (current) {
        list_node_t *next = current->next;
        free(current->data);
        free(current);
        current = next;
    }
    free(list);
}

bool list_empty(list_t *list) {
    return list ? list->head == NULL : true;
}

size_t list_length(list_t *list) {
    if (!list) return 0;
    
    size_t len = 0;
    list_node_t *current = list->head;
    while (current) {
        len++;
        current = current->next;
    }
    return len;
}

void list_append(list_t *list, void *data) {
    if (!list || !data) return;
    
    list_node_t *new_node = malloc(sizeof(list_node_t));
    if (!new_node) return;
    
    new_node->data = malloc(list->data_size);
    if (!new_node->data) {
        free(new_node);
        return;
    }
    memcpy(new_node->data, data, list->data_size);
    new_node->next = NULL;
    
    if (list_empty(list)) {
        list->head = new_node;
    } else {
        list_node_t *current = list->head;
        while (current->next) {
            current = current->next;
        }
        current->next = new_node;
    }
}

bool list_contains(list_t *list, void *data) {
    if (!list || !data) return false;
    
    list_node_t *current = list->head;
    while (current) {
        if (memcmp(current->data, data, list->data_size) == 0) {
            return true;
        }
        current = current->next;
    }
    return false;
}

size_t list_index(list_t *list, void *data) {
    if (!list || !data) return SIZE_MAX;
    
    size_t index = 0;
    list_node_t *current = list->head;
    while (current) {
        if (memcmp(current->data, data, list->data_size) == 0) {
            return index;
        }
        index++;
        current = current->next;
    }
    return SIZE_MAX;
}

void *list_pop(list_t *list) {
    if (!list || list_empty(list)) return NULL;
    
    list_node_t *last = NULL;
    list_node_t *current = list->head;
    
    if (!current->next) {
        list->head = NULL;
    } else {
        while (current->next->next) {
            current = current->next;
        }
        last = current->next;
        current->next = NULL;
    }
    
    void *data = malloc(list->data_size);
    if (!data) return NULL;
    
    memcpy(data, last ? last->data : current->data, list->data_size);
    if (last) {
        free(last->data);
        free(last);
    } else {
        free(current->data);
        free(current);
    }
    return data;
}

void list_remove(list_t *list, void *data) {
    if (!list || !data || list_empty(list)) return;
    
    list_node_t *prev = NULL;
    list_node_t *current = list->head;
    
    while (current) {
        if (memcmp(current->data, data, list->data_size) == 0) {
            if (prev) {
                prev->next = current->next;
            } else {
                list->head = current->next;
            }
            free(current->data);
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
}

void list_insert(list_t *list, size_t index, void *data) {
    if (!list || !data) return;
    
    list_node_t *new_node = malloc(sizeof(list_node_t));
    if (!new_node) return;
    
    new_node->data = malloc(list->data_size);
    if (!new_node->data) {
        free(new_node);
        return;
    }
    memcpy(new_node->data, data, list->data_size);
    
    if (index == 0 || list_empty(list)) {
        new_node->next = list->head;
        list->head = new_node;
        return;
    }
    
    list_node_t *current = list->head;
    size_t i = 0;
    while (current->next && i < index - 1) {
        current = current->next;
        i++;
    }
    new_node->next = current->next;
    current->next = new_node;
}

void list_print_int(list_t *list, FILE *stream) {
    if (!list || !stream) return;
    
    list_node_t *current = list->head;
    if (!current) {
        fprintf(stream, "NULL");
        return;
    }
    
    while (current) {
        fprintf(stream, "(%d)", *(int *)current->data);
        current = current->next;
        if (current) {
            fprintf(stream, " -> ");
        }
    }
    fprintf(stream, " -> NULL");
}
