# Horse Colic

## Data Set Information:

### 2 data files: 
horse-colic.data: 300 training instances 
horse-colic.test: 68 test instances 

Possible class attributes: 24 (whether lesion is surgical) 
-- others include: 23, 25, 26, and 27 

Many Data types: (continuous, discrete, and nominal)

## Attribute Information
<style>
table th:th:nth-of-type(3) {
    width: 400px;
}
</style>

| No.| Attribute| Value| Explanation
|:--------:|:---------:|:-------|:-------|
|1| surgery | 1,2 |  1 = Yes, it had surgery<br>2 = It was treated without surgery |
|2| Age |1,2|1 = Adult horse <br> 2 = Young (< 6 months) |
|3| Hospital Number | numeric id|the case number assigned to the horse (may not be unique if the horse is treated > 1 time) |
|4|rectal temperature |linear<br>in degrees celsius.|An elevated temp may occur due to infection.<br> temperature may be reduced when the animal is in late shock<br> normal temp is 37.8<br> this parameter will usually change as the problem progresses, eg. may start out normal, then become elevated because of the lesion, passing back through the normal range as the horse goes into shock |
|5|pulse|linear|the heart rate in beats per minute<br>is a reflection of the heart condition: 30 -40 is normal for adults<br>rare to have a lower than normal rate although athletic horses may have a rate of 20-25<br>animals with painful lesions or suffering from circulatory shock may have an elevated heart rate| 
|6|respiratory rate|linear|normal rate is 8 to 10<br>usefulness is doubtful due to the great fluctuations| 
|7| temperature of extremities|1 = Normal<br>2 = Warm<br>3 = Cool<br>4 = Cold|a subjective indication of peripheral circulation <br>cool to cold extremities indicate possible shock <br>hot extremities should correlate with an elevated rectal temp|
|8| peripheral pulse|subjective<br>1 = normal<br>2 = increased <br>3 = reduced <br>4 = absent|normal or increased p.p. are indicative of adequate circulation while reduced or absent indicate poor perfusion |
|9| mucous membranes|1 = normal pink<br>2 = bright pink<br>3 = pale pink<br>4 = pale cyanotic<br>5 = bright red / injected<br>6 = dark cyanotic|a subjective measurement of colour<br>1 and 2 probably indicate a normal or slightly increased circulation<br>3 may occur in early shock<br>4 and 6 are indicative of serious circulatory compromise<br>5 is more indicative of a septicemia 
|10|capillary refill time | 1 = < 3 seconds <br>2 = >= 3 seconds |a clinical judgement<br>The longer the refill, the poorer the circulation 
|11| pain | 1 = alert, no pain;2 = depressed;3 = intermittent mild pain;4 = intermittent severe pain <br>5 = continuous severe pain |a subjective judgement of the horse's pain level <br>should NOT be treated as a ordered or discrete variable! <br>In general, the more painful, the more likely it is to require surgery <br>prior treatment of pain may mask the pain level to some extent 
|12|peristalsis |1 = hypermotile <br>2 = normal <br>3 = hypomotile <br>4 = absent|an indication of the activity in the horse's gut. As the gut becomes more distended or the horse becomes more toxic, the activity decreases |
|13|abdominal distension |1 = none <br>2 = slight <br>3 = moderate <br>4 = severe |An IMPORTANT parameter.<br>an animal with abdominal distension is likely to be painful and have reduced gut motility.<br>a horse with severe abdominal distension is likely to require surgery just tio relieve the pressure 
|14| nasogastric tube |1 = none <br>2 = slight <br>3 = significant |this refers to any gas coming out of the tube<br>a large gas cap in the stomach is likely to give the horse discomfort|
|15| nasogastric reflux |1 = none <br>2 = > 1 liter <br>3 = < 1 liter |the greater amount of reflux, the more likelihood that there is some serious obstruction to the fluid passage from the rest of the intestine|
|16| nasogastric reflux PH| linear |scale is from 0 to 14 with 7 being neutral<br>normal values are in the 3 to 4 range |
|17| rectal examination |1 = normal <br>2 = increased <br>3 = decreased<br>4 = absent|feces<br>possible values <br>absent feces probably indicates an obstruction |
|18| abdomen|1 = normal <br>2 = other <br>3 = firm feces in the large intestine <br>4 = distended small intestine <br>5 = distended large intestine  |3 is probably an obstruction caused by a mechanical impaction and is normally treated medically <br>4 and 5 indicate a surgical lesion |
|19| packed cell volume |linear |the # of red cells by volume in the blood <br>normal range is 30 to 50. The level rises as the circulation becomes compromised or as the animal becomes dehydrated.| 
|20| total protein |linear|normal values lie in the 6-7.5 (gms/dL) range <br>the higher the value the greater the dehydration| 
|21| abdominocentesis appearance |1 = clear <br>2 = cloudy <br>3 = serosanguinous |a needle is put in the horse's abdomen and fluid is obtained from the abdominal cavity <br>normal fluid is clear while cloudy or serosanguinous indicates a compromised gut |
|22| abdomcentesis total protein|linear|the higher the level of protein the more likely it is to have a compromised gut. Values are in gms/dL 
|23| outcome|1 = lived <br>2 = died <br>3 = was euthanized |what eventually happened to the horse? 
|24| surgical lesion?|1 = Yes <br>2 = No |retrospectively, was the problem (lesion) surgical? <br>all cases are either operated upon or autopsied so that this value and the lesion type are always known| 
|25, 26, 27| type of lesion | Four numbers|Show as below|
|first number|site of lesion |1-00|1 = gastric<br>2 = sm intestine<br>3 = lg colon<br>4 = lg colon and cecum<br>5 = cecum <br>6 = transverse colon<br>7 = retum/descending colon<br> 8 = uterus <br>9 = bladder <br>11 = all intestinal sites <br>00 = none <br>|
|second number| type |1,2,3,4|1 = simple <br>2 = strangulation <br>3 = inflammation<br>4 = other 
|third number | subtype |1,2,0|1 = mechanical <br>2 = paralytic <br>0 = n/a <br>|
|fourth number | specific code |1-0|1 = obturation <br>2 = intrinsic <br>3 = extrinsic <br>4 = adynamic <br>5 = volvulus/torsion <br>6 = intussuption <br>7 = thromboembolic <br>8 = hernia <br>9 = lipoma/slenic incarceration <br>10 = displacement <br>0 = n/a |
|28|cp_data| 1 = Yes <br>2 = No|is pathology data present for this case? <br>this variable is of no significance since pathology data is not included or collected for these cases



