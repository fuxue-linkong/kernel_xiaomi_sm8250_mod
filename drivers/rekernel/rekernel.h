#ifndef _REKERNEL_H
#define _REKERNEL_H

#include <linux/sched.h>
#include <linux/sched/jobctl.h>
#include <linux/freezer.h>

#define PACKET_SIZE			128
#define MIN_USERAPP_UID			(10000)
#define MAX_SYSTEM_UID			(2000)

static inline bool line_is_frozen(struct task_struct *task)
{
	return frozen(task->group_leader) || freezing(task->group_leader);
}

int start_rekernel_server(void);
int send_netlink_message(char *msg, uint16_t len);

#endif /* _REKERNEL_H */