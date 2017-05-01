# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

# Create your views here.

import logging
import datetime
import random
from models import task_record
import json
import os
from demo import settings
import subprocess

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    taskId = random.randint(0, 99)
    logger.debug("index start...", extra={'taskId': taskId})
    logger.info("index start...", extra={'taskId': taskId})
    logger.warn("index start...", extra={'taskId': taskId})
    logger.error("index start...", extra={'taskId': taskId})
    response = render(request, 'index.html')
    logger.debug("index end...", extra={'taskId': taskId})
    logger.info("index end...", extra={'taskId': taskId})
    logger.warn("index end...", extra={'taskId': taskId})
    logger.error("index end...", extra={'taskId': taskId})
    return response

def submit(request):
    print 'submit ....'
    tr = task_record(status='0')
    tr.save()
    response = render(request, 'console.html',{'task':tr})    
    return response

def logs(request):
    taskId = request.GET.get('taskId')
    line = request.GET.get('line')
    
    print taskId
    if taskId is not None:
        tr = task_record.objects.get(id=taskId)
        if tr.status=='1':
            return JsonResponse({'code':'01'})
        elif tr.status=='2':
            return JsonResponse({'code':'02'})
        else:
            scriptname=os.path.join(settings.BASE_DIR,'get_log.sh')
            logfile=os.path.join(settings.BASE_DIR,'logs',taskId)
            res=execcommand([scriptname,logfile,line])
            print res
            ret = {'code':'00','errMsg':res[0],'logs':res[1]}
            #return HttpResponse(json.dumps(ret, ensure_ascii=False),content_type='application/json')
            return JsonResponse({'code':'00','errMsg':res[0],'logs':res[1]})

def execcommand(lst_cmd):
    cmd = ' '.join(lst_cmd)
    s = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdoutinfo, stderrinfo = s.communicate()
    return (stderrinfo, stdoutinfo)
    
