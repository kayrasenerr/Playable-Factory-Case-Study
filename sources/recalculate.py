"""Rebuild all ratios from the visually checked PDF transcription; stdlib only."""
import csv
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
FIELDS = ['spend_usd','impressions','playable_loads','first_interaction','end_card_reached','cta_clicks','conversions']
with (ROOT/'campaign_raw.csv').open() as f:
    raw = list(csv.DictReader(f))
assert len(raw) == 8
assert len({(r['campaign'],r['geo'],r['os']) for r in raw}) == 8
for r in raw:
    for k in FIELDS + ['avg_time_sec']:
        r[k] = float(r[k])
        assert r[k] >= 0
    assert r['impressions'] >= r['playable_loads'] >= r['first_interaction'] >= r['end_card_reached'] >= r['cta_clicks'] >= r['conversions']

def metrics(r):
    s,i,l,e,end,c,v = [r[k] for k in FIELDS]
    return {'CPM_USD':1000*s/i,'CPC_USD':s/c,'cost_per_conversion_USD':s/v,
            'load_rate_pct':100*l/i,'interaction_per_load_pct':100*e/l,
            'end_per_interaction_pct':100*end/e,'click_per_end_pct':100*c/end,
            'CTR_per_impression_pct':100*c/i,'conversion_per_click_pct':100*v/c,
            'conversions_per_1000_impressions':1000*v/i}

rows=[]
for r in raw:
    rows.append({'campaign':r['campaign'],'segment':r['geo']+' / '+r['os'],**{k:r[k] for k in FIELDS},**metrics(r)})
for dims in [('campaign',),('campaign','geo'),('campaign','os')]:
    groups=defaultdict(list)
    for r in raw: groups[tuple(r[d] for d in dims)].append(r)
    for key,group in groups.items():
        agg={k:sum(r[k] for r in group) for k in FIELDS}
        rows.append({'campaign':key[0],'segment':'TOTAL' if len(dims)==1 else dims[1]+'='+key[1],**agg,**metrics(agg)})
with (ROOT/'campaign_metrics.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

lines=['# Task 5.2: calculated audit tables','','Source: S02; produced by `data/recalculate.py`. Ratios use summed counts, not averages of row rates. No aggregated time metric is calculated because its denominator is unspecified.','']
for campaign in ['Puzzle Game X','Grocery App Y']:
    lines += ['## '+campaign,'','| Segment | Spend USD | Conversions | CPI / first-order CPA USD | CPM USD | Load % | Interaction / load % | End / interaction % | CTR / impressions % | Conversion / clicks % | Conv. / 1,000 impressions |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        if r['campaign']!=campaign:continue
        vals=[r['spend_usd'],r['conversions'],r['cost_per_conversion_USD'],r['CPM_USD'],r['load_rate_pct'],r['interaction_per_load_pct'],r['end_per_interaction_pct'],r['CTR_per_impression_pct'],r['conversion_per_click_pct'],r['conversions_per_1000_impressions']]
        lines.append('| '+r['segment']+' | '+' | '.join(f'{v:,.2f}' for v in vals)+' |')
    lines.append('')
(ROOT.parent/'09_Task_5_2_Calculated_Tables.md').write_text('\n'.join(lines))
for r in rows:
    if r['segment']=='TOTAL': print(r)
