
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import query
from django.db.models.fields import CommaSeparatedIntegerField
from django.db.models.functions.datetime import ExtractMonth
from django.db.models.query import QuerySet
from django.db.models.functions import ExtractYear
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import *
from .models import *

## /ProductionActual ##
def BlankProductionActualView(request):
    return render(request, "productionactual/index.html", )

## /ProductionActual/new/ ##
def NewProductionActualView(request):
    if request.method == 'POST':
        form = NewProductionActualForm(request.POST)
        if form.is_valid():
            # not save until form.save()
            form = form.save(commit=False)
            # set user that is logged in, to the user in the created production actual
            form.user = request.user    
            form.save()
            ## get the id of created, to go to that id as a url
            # newuuid = form.id
            # newuuidstr = str(newuuid)
            # baseurl = "/ProductionActual/"
            # need to create hourly
            create_hourly =  Hourly.objects.create(pk=str(form.id))
            #return HttpResponseRedirect(baseurl+newuuidstr)
            return HttpResponseRedirect("/ProductionActual/"+str(form.id))
    else:
        context ={}
        form = NewProductionActualForm()
        if form.is_valid():
            # not save until form.save()
            form = form.save(commit=False)
            # set user that is logged in to the form user
            form.user = request.user    
            form.save()

        context['form']= form
        return render(request, "productionactual/newproductionactual.html", context)

## /ProductionActual/newproduct/ ##
def NewProductView(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            # not save until form.save()
            form = form.save(commit=False)
            # set user that is logged in, to the user in the created production actual
            #form.user = request.user    
            form.save()
            ## get the id of created, to go to that id as a url
            # newuuid = form.id
            # newuuidstr = str(newuuid)
            # baseurl = "/ProductionActual/"
            # need to create hourly
            #create_hourly =  Hourly.objects.create(pk=str(form.id))
            #return HttpResponseRedirect(baseurl+newuuidstr)
            return HttpResponseRedirect("/ProductionActual/")
    else:
        context ={}
        form = NewProductForm()
        if form.is_valid():
            # not save until form.save()
            form = form.save(commit=False)
            # set user that is logged in to the form user
            #form.user = request.user    
            form.save()

        context['form']= form
        return render(request, "productionactual/newproduct.html", context)

## /ProductionActual/OpenRecent ##
# def OpenProductionActualView(request):
#     return render(request, "openproductionactual.html")
class OpenRecentProductionActualView(generic.ListView):
    template_name = 'productionactual/openrecentproductionactual.html'
    context_object_name = 'latest_pa_list'

    def get_queryset(self):
        """
        Return the last x created productionactuals (not including those set to be
        created in the future).
        """
        return ProductionActual.objects.filter(pa_date__lte=timezone.now()).order_by('-pa_date')[:50]

def OpenYearView(request):
    queryset = ProductionActual.objects.values_list('pa_date', flat=True)
    #yearlist = queryset.filter(pa_date__year='2021')
    yearlist = queryset.filter().annotate(year=ExtractYear('pa_date')).values('year')
    context = {}
    dbgcontext ={}
    
    # this removes any duplicate item from list
    res = [] 
    for i in yearlist: 
        if i not in res: 
            res.append(i)
    yearlist = res

    context["yearlist"] = yearlist
    dbgcontext["yearlist"] = yearlist




    #dbgcontext["c"] = context
    # everything that goes to context goes into debug
    
    debug_out = "debug: "+ str(dbgcontext)
    context["debug_out"] = debug_out

    return render(request, "productionactual/openyear.html", context)


def OpenMonthView(request, year):
    queryset = ProductionActual.objects.values_list('pa_date', flat=True)
    monthlist = queryset.filter(pa_date__year=year)
    x = monthlist.filter().annotate(month=ExtractMonth('pa_date')).values('month')

    # removeing duplicates from list
    res = [] 
    for i in x: 
        if i not in res: 
            res.append(i)
    monthlist = res

    context = {}
    dbgcontext ={}
    
    #dbgcontext["x"] = x
    context["year"] = year
    context["monthlist"] = monthlist
    dbgcontext["monthlist"] = monthlist

    #dbgcontext["c"] = context
    # everything that goes to context goes into debug
    
    debug_out = "debug: "+ str(dbgcontext)
    context["debug_out"] = debug_out

    return render(request, "productionactual/openmonth.html", context)

def OpenDepartmentView(request, year, month):
    queryset = Department.objects.all()
    deplist = queryset.filter()
    

    # removeing duplicates from list
    res = [] 
    for i in deplist: 
        if i not in res: 
            res.append(i)
    deplist = res

    context = {}
    dbgcontext ={}
    
    #dbgcontext["x"] = x
    context["year"] = year
    context["month"] = month
    context["deplist"] = deplist
    dbgcontext["deplist"] = deplist

    #dbgcontext["c"] = context
    # everything that goes to context goes into debug
    
    debug_out = "debug: "+ str(dbgcontext)
    context["debug_out"] = debug_out

    return render(request, "productionactual/opendepartment.html", context)

def OpenLineView(request, year, month, department):
    queryset = AssemblyLine.objects.all()
    linelist = queryset.filter()
    

    # removeing duplicates from list
    res = [] 
    for i in linelist: 
        if i not in res: 
            res.append(i)
    linelist = res

    context = {}
    dbgcontext ={}
    
    #dbgcontext["x"] = x
    context["year"] = year
    context["month"] = month
    context["department"] = department
    context["linelist"] = linelist
    
    dbgcontext["context_debug"] = context

    #dbgcontext["c"] = context
    # everything that goes to context goes into debug
    
    debug_out = "debug: "+ str(dbgcontext)
    context["debug_out"] = debug_out

    return render(request, "productionactual/openline.html", context)

def OpenProductionActualView(request, year, month, department, line):
    queryset = ProductionActual.objects.all()
    querysetyear = queryset.filter(pa_date__year=year)
    querysetmonth = querysetyear.filter(pa_date__month=month)
    palist = querysetmonth.filter(assembly_line_number__line_name=line)

    #palist = querysetmonth
    ## this is how we did it last time

    # queryset = ProductionActual.objects.values_list('pa_date', flat=True)
    # monthlist = queryset.filter(pa_date__year=year)
    # x = monthlist.filter().annotate(month=ExtractMonth('pa_date')).values('month')

    context = {}
    dbgcontext ={}
    
    #dbgcontext["x"] = x
    context["year"] = year
    context["month"] = month
    context["department"] = department
    context["line"] = line
    context["palist"] = palist
    dbgcontext["palist"] = palist

    #dbgcontext["c"] = context
    # everything that goes to context goes into debug
    
    debug_out = "debug: "+ str(dbgcontext)
    context["debug_out"] = debug_out

    return render(request, "productionactual/openproductionactual.html", context)

## /ProductionActual/20a0904a-ba5f-4a67-a163-03110dae00ce/ ## ex: an opened production actual
def ProductionActualView(request, pk):
    # dict for inital data with field names as keys
    context ={}
    dbgcontext ={}
    Production_Actual = get_object_or_404(ProductionActual, pk=pk)
    context["ProductionActual"] = Production_Actual
    Hourly_Count = Hourly.objects.get(ProductionActual=pk)
    context["hourly"] = Hourly_Count

    ## make hourly
    h1=int(Hourly_Count.hour1)
    h2=int(Hourly_Count.hour2)
    h3=int(Hourly_Count.hour3)
    h4=int(Hourly_Count.hour4)
    h5=int(Hourly_Count.hour5)
    h6=int(Hourly_Count.hour6)
    h7=int(Hourly_Count.hour7)
    h8=int(Hourly_Count.hour8)
    h9=int(Hourly_Count.hour9)
    h10=int(Hourly_Count.hour10)
    h11=int(Hourly_Count.hour11)
    h12=int(Hourly_Count.hour12)
    ## Cumulative Pcs. calculator
    h1c=h1
    h2c=h1+h2
    h3c=h1+h2+h3
    h4c=h1+h2+h3+h4
    h5c=h1+h2+h3+h4+h5
    h6c=h1+h2+h3+h4+h5+h6
    h7c=h1+h2+h3+h4+h5+h6+h7
    h8c=h1+h2+h3+h4+h5+h6+h7+h8
    h9c=h1+h2+h3+h4+h5+h6+h7+h8+h9
    h10c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10
    h11c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11
    h12c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12
    hourly_calc={
        'hour1calc': h1c,
        'hour2calc': h2c,
        'hour3calc': h3c,
        'hour4calc': h4c,
        'hour5calc': h5c,
        'hour6calc': h6c,
        'hour7calc': h7c,
        'hour8calc': h8c,
        'hour9calc': h9c,
        'hour10calc': h10c,
        'hour11calc': h11c,
        'hour12calc' : h12c
    }
    context["hourcalc"] = hourly_calc
    sethour={
        'hour1': h1,
        'hour2': h2,
        'hour3': h3,
        'hour4': h4,
        'hour5': h5,
        'hour6': h6,
        'hour7': h7,
        'hour8': h8,
        'hour9': h9,
        'hour10': h10,
        'hour11': h11,
        'hour12': h12,
        }
    context["sethour"] = sethour

    hourly_form = HourlyForm(request.POST or None, initial=sethour)
    if hourly_form.is_valid():
        # not save until form.save()
        hourly_form = hourly_form.save(commit=False)
        # link the hourly object to the correct productionactual uuid
        hourly_form.ProductionActual_id = pk
        hourly_form.save()
        return HttpResponseRedirect("/ProductionActual/"+str(pk))
    context["hourlyform"] = hourly_form

    ## make runs
    # get runs for single production actual
    def MakeRuns(*args):
        RunFilter = Run.objects.filter(ProductionActual=pk)
        for rn in args:
            RunFilter = RunFilter.filter(number=rn)
            Runs = RunFilter.get()

            Runs_number = Runs.number
            Runs_partal_start = Runs.partal_start
            Runs_partal_end = Runs.partal_end
            Runs_finnished_goods = Runs.finished_goods
            Runs_kanban_count = Runs.kanban_count
            # this dont work
            Runs_product_number = Runs.product_number
            Runs_start_time = Runs.start_time
            Runs_finish_time = Runs.finish_time
            Runs_plan_down_time = Runs.plan_down_time
            Runs_net_ope_time = Runs.net_ope_time
            Runs_plan_quanity = Runs.plan_quanity
            Runs_result_quanity = Runs.result_quanity
            Runs_scrap_quanity = Runs.scrap_quanity
            Runs_repair_quanity = Runs.repair_quanity
            Runs_analysis_quanity = Runs.analysis_quanity
            Runs_quarantine_quanity = Runs.quarantine_quanity
            Runs_cabbage_patch_quanity = Runs.cabbage_patch_quanity
            Runs_unplan_downtime = Runs.unplan_downtime
            Runs_standard_time = Runs.standard_time
            Runs_oa = Runs.oa
            Runs_oa_without_downtime = Runs.oa_without_downtime

            # overrides for testing
            tote=90
            Runs_plan_quanity = Runs_kanban_count * tote

            #timediff = Runs_finish_time - Runs_start_time
            # total_seconds=time_delta.total_seconds()
            # Runs_net_ope_time = round(total_seconds/60)


            dbgcontext["starttimes"] = Runs_start_time
            dbgcontext["finishtimes"] = Runs_finish_time
            dbgcontext["timedelta"] = type(time_delta)
            setrun={
                'number': Runs_number,
                'partal_start': Runs_partal_start,
                'partal_end': Runs_partal_end,
                'finished_goods': Runs_finnished_goods,
                'kanban_count': Runs_kanban_count,
                'product_number': Runs_product_number,
                'start_time': Runs_start_time,
                'finish_time': Runs_finish_time,
                'plan_down_time': Runs_plan_down_time,
                'net_ope_time': Runs_net_ope_time,
                'plan_quanity': Runs_plan_quanity,
                'result_quanity': Runs_result_quanity,
                'scrap_quanity': Runs_scrap_quanity,
                'repair_quanity': Runs_repair_quanity,
                'analysis_quanity': Runs_analysis_quanity,
                'quarantine_quanity': Runs_quarantine_quanity,
                'cabbage_patch_quanity': Runs_cabbage_patch_quanity,
                'unplan_downtime': Runs_unplan_downtime,
                'standard_time': Runs_standard_time,
                'oa': Runs_oa,
                'oa_without_downtime': Runs_oa_without_downtime,
                }

            run_form = RunForm(request.POST or None, initial=setrun)
            if run_form.is_valid():
                # not save until form.save()
                run_form = run_form.save(commit=False)
                # link the run object to the correct productionactual uuid
                run_form.ProductionActual_id = pk
                run_form.save()
                return HttpResponseRedirect("/ProductionActual/"+str(pk))
            rns=str(rn) 
            context["runform"+rns] = run_form

    RunsExist=True
    try:
        
        MakeRuns(4)
        MakeRuns(3)
        MakeRuns(2)
        MakeRuns(1)
    except:
        try:
            
            MakeRuns(3)
            MakeRuns(2)
            MakeRuns(1)
        except:
            try:
                
                MakeRuns(2)
                MakeRuns(1)
            except:
                try:
                    
                    MakeRuns(1)
                except:
                    RunsExist=False

    context["RunsExist"] = RunsExist

    #dbgcontext["c"] = context
    # everything that goes to context goes into debug
    #dbgcontext = context

    debug_out = "debug: "+ str(dbgcontext)
    context["debug_out"] = debug_out
    return render(request, "productionactual/productionactual.html", context)

##################################################

##################################################

##################################################

##################################################

## /ProductionActual/20a0904a-ba5f-4a67-a163-03110dae00ce/LostTime ## ex: lost time for an opened production actual
def LostTimeView(request, pk):
    # dict for inital data with field names as keys
    context ={}
    Production_Actual = get_object_or_404(ProductionActual, pk=pk)
    context["ProductionActual"] = Production_Actual
    Hourly_Count = Hourly.objects.get(ProductionActual=pk)
    context["hourly"] = Hourly_Count
    ## make hourly
    h1=int(Hourly_Count.hour1)
    h2=int(Hourly_Count.hour2)
    h3=int(Hourly_Count.hour3)
    h4=int(Hourly_Count.hour4)
    h5=int(Hourly_Count.hour5)
    h6=int(Hourly_Count.hour6)
    h7=int(Hourly_Count.hour7)
    h8=int(Hourly_Count.hour8)
    h9=int(Hourly_Count.hour9)
    h10=int(Hourly_Count.hour10)
    h11=int(Hourly_Count.hour11)
    h12=int(Hourly_Count.hour12)
    ## Cumulative Pcs. calculator
    h1c=h1
    h2c=h1+h2
    h3c=h1+h2+h3
    h4c=h1+h2+h3+h4
    h5c=h1+h2+h3+h4+h5
    h6c=h1+h2+h3+h4+h5+h6
    h7c=h1+h2+h3+h4+h5+h6+h7
    h8c=h1+h2+h3+h4+h5+h6+h7+h8
    h9c=h1+h2+h3+h4+h5+h6+h7+h8+h9
    h10c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10
    h11c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11
    h12c=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12
    hourly_calc={
        'hour1calc': h1c,
        'hour2calc': h2c,
        'hour3calc': h3c,
        'hour4calc': h4c,
        'hour5calc': h5c,
        'hour6calc': h6c,
        'hour7calc': h7c,
        'hour8calc': h8c,
        'hour9calc': h9c,
        'hour10calc': h10c,
        'hour11calc': h11c,
        'hour12calc' : h12c
    }
    context["hourcalc"] = hourly_calc
    sethour={
        'hour1': h1,
        'hour2': h2,
        'hour3': h3,
        'hour4': h4,
        'hour5': h5,
        'hour6': h6,
        'hour7': h7,
        'hour8': h8,
        'hour9': h9,
        'hour10': h10,
        'hour11': h11,
        'hour12': h12,
        }
    context["sethour"] = sethour
    
    ## Standard Time is quanity produced muliplied by the Cycle time divied by amount of time (60minutes)
    ct1 = 5
    ct2 = 5
    ct3 = 5
    ct4 = 5
    ct5 = 5
    ct6 = 5
    ct7 = 5
    ct8 = 5
    ct9 = 5
    ct10 = 5
    ct11 = 5
    ct12 = 5

    
    cycle_time ={
        'cycle_time1': ct1,
        'cycle_time2': ct2,
        'cycle_time3': ct3,
        'cycle_time4': ct4,
        'cycle_time5': ct5,
        'cycle_time6': ct6,
        'cycle_time7': ct7,
        'cycle_time8': ct8,
        'cycle_time9': ct9,
        'cycle_time10': ct10,
        'cycle_time11': ct11,
        'cycle_time12': ct12,
    }

    context["cycle_time"] = cycle_time

    st1 = round(ct1 * h1 / 60)
    st2 = round(ct2 * h2 / 60)
    st3 = round(ct3 * h3 / 60)
    st4 = round(ct4 * h4 / 60)
    st5 = round(ct5 * h5 / 60)
    st6 = round(ct6 * h6 / 60)
    st7 = round(ct7 * h7 / 60)
    st8 = round(ct8 * h8 / 60)
    st9 = round(ct9 * h9 / 60)
    st10 = round(ct10 * h10 / 60)
    st11 = round(ct11 * h11 / 60)
    st12 = round(ct12 * h12 / 60)
    
    StandardTime ={
        'StandardTime1': st1,
        'StandardTime2': st2,
        'StandardTime3': st3,
        'StandardTime4': st4,
        'StandardTime5': st5,
        'StandardTime6': st6,
        'StandardTime7': st7,
        'StandardTime8': st8,
        'StandardTime9': st9,
        'StandardTime10': st10,
        'StandardTime11': st11,
        'StandardTime12': st12,
    }
    context["StandardTime"] = StandardTime

    # define vars for planned downtime

    pdt1 = 8
    pdt2 = 0
    pdt3 = 18
    pdt4 = 0
    pdt5 = 33
    pdt6 = 0
    pdt7 = 18
    pdt8 = 0
    pdt9 = 18
    pdt10 = 8
    pdt11 = 0
    pdt12 = 0

    PlannedDownTime ={
        'PlannedDownTime1': pdt1,
        'PlannedDownTime2': pdt2,
        'PlannedDownTime3': pdt3,
        'PlannedDownTime4': pdt4,
        'PlannedDownTime5': pdt5,
        'PlannedDownTime6': pdt6,
        'PlannedDownTime7': pdt7,
        'PlannedDownTime8': pdt8,
        'PlannedDownTime9': pdt9,
        'PlannedDownTime10': pdt10,
        'PlannedDownTime11': pdt11,
        'PlannedDownTime12': pdt12,
    }
    context["PlannedDowntime"] = PlannedDownTime

    # define vars for unplanned downtime

    updt1 = 8
    updt2 = 3
    updt3 = 4
    updt4 = 5
    updt5 = 6
    updt6 = 7
    updt7 = 10
    updt8 = 3
    updt9 = 4
    updt10 = 8
    updt11 = 0
    updt12 = 0

    UnPlannedDownTime ={
        'UnPlannedDownTime1': updt1,
        'UnPlannedDownTime2': updt2,
        'UnPlannedDownTime3': updt3,
        'UnPlannedDownTime4': updt4,
        'UnPlannedDownTime5': updt5,
        'UnPlannedDownTime6': updt6,
        'UnPlannedDownTime7': updt7,
        'UnPlannedDownTime8': updt8,
        'UnPlannedDownTime9': updt9,
        'UnPlannedDownTime10': pdt10,
        'UnPlannedDownTime11': pdt11,
        'UnPlannedDownTime12': pdt12,
    }
    context["UnPlannedDowntime"] = UnPlannedDownTime

    ## Lost time is Planned Down Time + UnPlanned Down Time + Standard time ) minus the time (60minutes)

    lt1 = pdt1 + updt1 + st1 - 60
    lt2 = pdt2 + updt2 + st2 - 60
    lt3 = pdt3 + updt3 + st3 - 60
    lt4 = pdt4 + updt4 + st4 - 60
    lt5 = pdt5 + updt5 + st5 - 60
    lt6 = pdt6 + updt6 + st6 - 60
    lt7 = pdt7 + updt7 + st7 - 60
    lt8 = pdt8 + updt8 + st8 - 60
    lt9 = pdt9 + updt9 + st9 - 60
    lt10 = pdt10 + updt10 + st10 - 60
    lt11 = pdt11 + updt11 + st11 - 60
    lt12 = pdt12 + updt12 + st12 - 60

    LostTime ={
            'LostTime1': lt1,
            'LostTime2': lt2,
            'LostTime3': lt3,
            'LostTime4': lt4,
            'LostTime5': lt5,
            'LostTime6': lt6,
            'LostTime7': lt7,
            'LostTime8': lt8,
            'LostTime9': lt9,
            'LostTime10': lt10,
            'LostTime11': lt11,
            'LostTime12': lt12,
        }
    context["LostTime"] = LostTime

    ## net operation is the hour minutes minus any planned Downtime, this is needed to calculate OA,100% and 85%

    netop1 = 60 - pdt1
    netop2 = 60 - pdt2
    netop3 = 60 - pdt3
    netop4 = 60 - pdt4
    netop5 = 60 - pdt5
    netop6 = 60 - pdt6
    netop7 = 60 - pdt7
    netop8 = 60 - pdt8
    netop9 = 60 - pdt9
    netop10 = 60 - pdt10
    netop11 = 60 - pdt11
    netop12 = 60 - pdt12

    ## OA is standard time divided by the net operation

    oa1 = str("{:.3g}".format(st1 / netop1 * 100)) + "%"
    oa2 = str("{:.3g}".format(st2 / netop2 * 100)) + "%"
    oa3 = str("{:.3g}".format(st3 / netop3 * 100)) + "%"
    oa4 = str("{:.3g}".format(st4 / netop4 * 100)) + "%"
    oa5 = str("{:.3g}".format(st5 / netop5 * 100)) + "%"
    oa6 = str("{:.3g}".format(st6 / netop6 * 100)) + "%"
    oa7 = str("{:.3g}".format(st7 / netop7 * 100)) + "%"
    oa8 = str("{:.3g}".format(st8 / netop8 * 100)) + "%"
    oa9 = str("{:.3g}".format(st9 / netop9 * 100)) + "%"
    oa10 = str("{:.3g}".format(st10 /netop10 * 100)) + "%"
    oa11 = str("{:.3g}".format(st11 / netop11 * 100)) + "%"
    oa12 = str("{:.3g}".format(st12 / netop12 * 100)) + "%"

    oa ={
            'oa1': oa1,
            'oa2': oa2,
            'oa3': oa3,
            'oa4': oa4,
            'oa5': oa5,
            'oa6': oa6,
            'oa7': oa7,
            'oa8': oa8,
            'oa9': oa9,
            'oa10': oa10,
            'oa11': oa11,
            'oa12': oa12,
        }
    context["oa"] = oa

    ## 100% is time60 / cycletime) times ( net operation )

    oneh1 = round(60 / ct1 * netop1)
    oneh2 = round(60 / ct2 * netop2)
    oneh3 = round(60 / ct3 * netop3)
    oneh4 = round(60 / ct4 * netop4)
    oneh5 = round(60 / ct5 * netop5)
    oneh6 = round(60 / ct5 * netop6)
    oneh7 = round(60 / ct7 * netop7)
    oneh8 = round(60 / ct8 * netop8)
    oneh9 = round(60 / ct9 * netop9)
    oneh10 = round(60 / ct10 * netop10)
    oneh11 = round(60 / ct11 * netop11)
    oneh12 = round(60 / ct12 * netop12)

    oneh ={
            '1': oneh1,
            '2': oneh2,
            '3': oneh3,
            '4': oneh4,
            '5': oneh5,
            '6': oneh6,
            '7': oneh7,
            '8': oneh8,
            '9': oneh9,
            '10': oneh10,
            '11': oneh11,
            '12': oneh12,
        }
    context["oneh"] = oneh

    ## 85% is 100*0.85

    eightyfive1 = round(oneh1 * 0.85)
    eightyfive2 = round(oneh2 * 0.85)
    eightyfive3 = round(oneh3 * 0.85)
    eightyfive4 = round(oneh4 * 0.85)
    eightyfive5 = round(oneh5 * 0.85)
    eightyfive6 = round(oneh6 * 0.85)
    eightyfive7 = round(oneh7 * 0.85)
    eightyfive8 = round(oneh8 * 0.85)
    eightyfive9 = round(oneh9 * 0.85)
    eightyfive10 = round(oneh10 * 0.85)
    eightyfive11 = round(oneh11 * 0.85)
    eightyfive12 = round(oneh12 * 0.85)

    eightyfive ={
            '1': eightyfive1,
            '2': eightyfive2,
            '3': eightyfive3,
            '4': eightyfive4,
            '5': eightyfive5,
            '6': eightyfive6,
            '7': eightyfive7,
            '8': eightyfive8,
            '9': eightyfive9,
            '10': eightyfive10,
            '11': eightyfive11,
            '12': eightyfive12,
        }
    context["eightyfive"] = eightyfive

    ## debug ouput
    debug_out = "debug: "
    context["debug_out"] = debug_out
    return render(request, "productionactual/losttime.html", context)
