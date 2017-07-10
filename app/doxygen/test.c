/**
* Copyright @ 2014 - 2015 Suntec Software(Shanghai) Co., Ltd.
* All Rights Reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are NOT permitted except as agreed by
* Suntec Software(Shanghai) Co., Ltd.
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*/

#include <bdaddr.h>
#include <stdlib.h>
#include <string.h>
#include <pro_source.h>
#include "stdio.h"
#include "pro_sink.h"
#include "atparse.h"
#include "pro_sppc_if.h"
#include "pro_spp_common.h"
#include "pro_sppc_private.h"

#define MAKE_SPP_MESSAGE_WITH_LEN(TYPE, LEN) TYPE##_T *message = (TYPE##_T *) PanicUnlessMalloc(sizeof(TYPE##_T) + LEN);
#include <pro_stream.h>

/*****************************************************************************/


/*!
    @brief PRO_sppConnectRequest

    @param bd_addr
    @param security_channel
    @param sppId

    //TODO:
*/
void PRO_sppConnectRequest(const bdaddr *bd_addr, const uint16 security_channel, const uint8 sppId)
{
	pro_sppConnectRequest(bd_addr,security_channel,sppId);
}

/****************************************************************************
NAME
    PRO_sppcRegInstanceRequest

DESCRIPTION
    Used this to register spp information.

RETURNS
    status
*/
uint8 PRO_sppcRegInstanceRequest(Task theAppTask, uint8 sppId, const uint16 max_payload_size,
													const uint8 sdp_index, const uint8 sdp_len, const uint8 *sdp)
{
    return pro_sppcRegInstanceRequest(theAppTask,sppId,max_payload_size,sdp_index,sdp_len,sdp);
}


/****************************************************************************
NAME
    PRO_sppcUnregInstanceRequest

DESCRIPTION
    Used this to unregister the request id's UUID information

RETURNS
    status
*/

/*!
    @brief PRO_sppcUnregInstanceRequest

    @param sppId

    //TODO:
*/
uint8 PRO_sppcUnregInstanceRequest(const uint8 sppId)
{
    return pro_sppcUnregInstanceRequest(sppId);
}


/****************************************************************************
NAME
    PRO_sppGetUUID

DESCRIPTION
    Used this to get the SPP device's UUID information.

RETURNS
    status.
*/

/*!
    @brief PRO_sppGetUUID

    @param sppId
    @param uuidLen
    @param uuid

    //TODO:
*/
bool PRO_sppGetUUID(uint8 sppId, uint16 *uuidLen, uint8 *uuid)
{
    return pro_sppGetUUID(sppId,uuidLen,uuid);
}

/****************************************************************************
NAME
    PRO_sppQueryUUID

DESCRIPTION
    Used this to query if the uuid supported by remote address.

RETURNS
    status.
*/

/*!
    @brief PRO_sppQueryUUID

    @param addr
    @param sdp_index
    @param uuidLen
    @param uuid

    //TODO:
*/
bool PRO_sppQueryUUID(bdaddr addr, uint8 sdp_index, uint16 uuidLen, uint8 *uuid)
{
    return pro_sppQueryUUID(addr,sdp_index,uuidLen,uuid);
}

/****************************************************************************
NAME
    PRO_sppcConnectRequest

DESCRIPTION
    Used this to connect spp instance.

RETURNS
    status
*/

/*!
    @brief PRO_sppcConnectRequest

    @param theAppTask
    @param bd_addr
    @param uuidLen
    @param uuid
    @param scn
    @param max_payload_size
    @param priority

    //TODO:
*/
uint8 PRO_sppcConnectRequest(Task theAppTask, bdaddr bd_addr, uint16 uuidLen, const uint8 *uuid, uint8 scn, const uint16 max_payload_size, uint8* priority)
{
    return pro_sppcConnectRequest(theAppTask,bd_addr,uuidLen,uuid,scn,max_payload_size,priority);
}
/****************************************************************************
NAME
    PRO_sppcCancelConRequest

DESCRIPTION
    Used this to cancel connect spp instance.

RETURNS
    status
*/

/*!
    @brief PRO_sppcCancelConRequest

    @param theAppTask
    @param sppId

    //TODO:
*/
uint8 PRO_sppcCancelConRequest(Task theAppTask, uint8 sppId )
{
    return pro_sppcCancelConRequest(theAppTask,sppId);
}


/****************************************************************************
NAME
    PRO_sppMessageSend

DESCRIPTION
    send message to spp task.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppMessageSend

    @param id
    @param message

    //TODO:
*/
void PRO_sppMessageSend(MessageId id, void *message)
{
	MessageSend(sppcommon->client_task, id, message);
}

/****************************************************************************
NAME
    PRO_sppHandleReceivedData

DESCRIPTION
    Called when we get an indication from the firmware that there's more data
    received and waiting in the RFCOMM buffer. Parse it.

RETURNS
    void
*/

/*!
    @brief PRO_sppHandleReceivedData

    @param spp
    @param source
    @param sourceLen

    //TODO:
*/
void PRO_sppHandleReceivedData(SPP *spp, uint8* source, uint16 sourceLen)
{
    BtPmemFree(source);
#if 0
    uint16 len;
    len = SourceSize(source);
    SourceDrop(source, len);
	PRO_sppSetLinkPriorityBySink(spp, StreamSinkFromSource(source));

	/* Only bother parsing if there is something to parse */
	while (len > 0)
	{
		/*if host have't buffer, resend mesage*/
		if (PRO_getSppLockInd())
		{
			MessageMoreData *p = (MessageMoreData*)PanicUnlessMalloc(sizeof(MessageMoreData));
			p->source = source;
			MessageSend(&sppcommon->taskForClient, MESSAGE_MORE_DATA, (void*)p);
			return;
		}

		/*Keepink parsing while we have data in the buffer */
		sppcommon->sppId = spp->sppId;

		if (!parseSource(source, (Task)sppcommon, sppcommon->client_task, (uint8)at_type_spp))
			break;

		/* Check we have more data to parse */
		len = SourceSize(source);
	}
#endif
}

/****************************************************************************
NAME
    PRO_sppUnlockInd

DESCRIPTION
    unlock source.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppUnlockInd

    //TODO:
*/
void PRO_sppUnlockInd(void)
{
	sppcommon->indLock = FALSE;
}

/****************************************************************************
NAME
    PRO_sppLockInd

DESCRIPTION
    lock source.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppLockInd

    //TODO:
*/
void PRO_sppLockInd(void)
{
	sppcommon->indLock = TRUE;
}


/****************************************************************************
NAME
    PRO_getSppLockInd

DESCRIPTION
    get source lock state.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_getSppLockInd

    //TODO:
*/
uint8 PRO_getSppLockInd(void)
{
	if(NULL != sppcommon)
	{
		return sppcommon->indLock;
	}
	else
	{
		return FALSE;
	}
}



/****************************************************************************
NAME
    PRO_sppHandleUnrecognised

DESCRIPTION
    Handle unrecognised AG return data.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppHandleUnrecognised

    @param data
    @param length
    @param task

    //TODO:
*/
void PRO_sppHandleUnrecognised(const uint8 *data, uint16 length, Task task)
{
    uint8 priority = (uint8)PRO_sppGetSessionInstance((SPP *) task);
    atLockInd(at_type_spp);
    if(length > AT_MAX_UNRECOGNISED_DATA_LENGTH) length = (uint16)AT_MAX_UNRECOGNISED_DATA_LENGTH;
    {
        MAKE_SPP_MESSAGE(SPP_BLUETEC_UNRECOGNISED_AT_CMD_IND);
        message->priority = priority;
        message->size_data = length;
        memcpy(message->data, data, length);
        PRO_sppMessageSend(SPP_BLUETEC_UNRECOGNISED_AT_CMD_IND, message);
    }
}

/****************************************************************************
NAME
    sppCmdAckReceived

DESCRIPTION
    Handle the AT Ack message include OK/Error/Timeout

RETURNS
    void
*/

/*!
    @brief pro_sppCmdAckReceived

    @param task
    @param status

    //TODO:
*/
static void pro_sppCmdAckReceived(Task task, spp_common_status status)
{
	SPP* sppctask = (SPP *)task;
	uint16 cmf_id = 0;
	uint8 priority = (uint8)PRO_sppGetSessionInstance(sppctask);
    Sink sink = PRO_sppGetLinkSink(sppctask, priority);

	switch(sppctask->at_cmd_resp_pending[priority])
	{
		case sppCharSetPending:
			cmf_id = SPP_BLUETEC_INTERNEL_CHARSET_CFM;
			break;
        case sppPbdlPending:
        case sppPbdlEntryPending:
            cmf_id = AT_INTERNEL_PBDL_CFM; /*General PBDL cfm*/
            break;
		case sppSmsLSWAtPending:
		case sppSmsAtPending:
			cmf_id = AT_INTERNEL_SMS_CFM;  /*General SMS cfm*/
			break;
		default:
			break;
	}

	MessageCancelAll(&sppcommon->taskForClient, priority + SPP_INTERNAL_TIMEOUT_IND_0);

    if(cmf_id)
	{
        #if 0
		MAKE_SPP_MESSAGE_WITH_LEN(AT_PBDL_SMS_CMD_CFM, 0);
        message->priority = priority;
        message->atType = at_type_spp;
		message->status = status;
		PRO_sppMessageSend(cmf_id, message);
		PRO_sppResetPendingState(sppctask);
        #endif
	}

    /* Try to send the next AT cmd in the buffer if possible */
    /*if(sink)
        sppSendAtCmdPro(sppctask, SinkClaim(sink, 0), SinkMap(sink));*/
}

/****************************************************************************
NAME
    PRO_sppHandleOk

DESCRIPTION
    Handle the AT OK indication sent by the AG.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppHandleOk

    @param task

    //TODO:
*/
void PRO_sppHandleOk(Task task)
{
    sppCmdAckReceived(task, spp_sucess);
}



/****************************************************************************
NAME
    PRO_sppHandleError

DESCRIPTION
    Handle the AT Error indication sent by the AG.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppHandleError

    @param task

    //TODO:
*/
void PRO_sppHandleError(Task task)
{
    sppCmdAckReceived(task, spp_fail);
}

/****************************************************************************
NAME
    PRO_sppHandleSpecialChar

DESCRIPTION
    Handle the sent/write message at cmd

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppHandleSpecialChar

    @param task

    //TODO:
*/
bool PRO_sppHandleSpecialChar(Task task)
{
    SPP *spp = (SPP *)task;
    uint8 priority = PRO_sppGetSessionInstance(spp);

    if((spp->at_cmd_resp_pending[priority] == sppSmsAtPending)||(spp->at_cmd_resp_pending[priority] == sppSmsLSWAtPending))
    {
        #if 0
    	MAKE_SPP_MESSAGE_WITH_LEN(AT_PBDL_SMS_CMD_CFM, 0);
        message->priority = priority;
        message->atType = at_type_spp;
    	message->status = spp_sucess;
    	PRO_sppMessageSend(AT_INTERNEL_SMS_CFM, message);
        #endif
        return TRUE;
    }
    else
        return FALSE;
}



/****************************************************************************
NAME
    PRO_sppHandleWaitAtTimeout

DESCRIPTION
    Handle the AT timeout

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppHandleWaitAtTimeout

    @param spp

    //TODO:
*/
void PRO_sppHandleWaitAtTimeout(SPP *spp)
{
    sppCmdAckReceived((Task)spp, spp_timeout);
}

/****************************************************************************
NAME
    PRO_sppCancelTimer

DESCRIPTION
    cancel the spp timer

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppCancelTimer

    @param task

    //TODO:
*/
void PRO_sppCancelTimer(Task task)
{
	/*MessageCancelAll(&sppc->task, SPP_INTERNAL_TIMEOUT_IND_0);*/
	SPP* spp = (SPP *)task;
    uint8 priority = (uint8)PRO_sppGetSessionInstance(spp);

	MessageCancelAll(&sppcommon->taskForClient, priority + SPP_INTERNAL_TIMEOUT_IND_0);
}

/****************************************************************************
NAME
    PRO_sppResetTimer

DESCRIPTION
    reset the spp timer

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppResetTimer

    @param task
    @param time

    //TODO:
*/
void PRO_sppResetTimer(Task task, uint32 time)
{
	uint32 timer = time;
	SPP* spp = (SPP *)task;
    uint8 priority = (uint8)PRO_sppGetSessionInstance(spp);
    MessageId timeout_evt_id = priority + SPP_INTERNAL_TIMEOUT_IND_0;

	MessageCancelAll(&sppcommon->taskForClient, timeout_evt_id);
	MessageSendLater(&sppcommon->taskForClient, timeout_evt_id, 0, timer);
}


/****************************************************************************
NAME
    PRO_sppResetPendingState

DESCRIPTION
    reset pending state.

AT INDICATION
    OK

RETURNS
    void
*/

/*!
    @brief PRO_sppResetPendingState

    @param spp

    //TODO:
*/
void PRO_sppResetPendingState(SPP* spp)
{
	spp->at_cmd_resp_pending[spp->sppId] = sppNoCmdPending;
}




