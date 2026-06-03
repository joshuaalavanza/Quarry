"""One-off ingestion script for medium Expression of Ideas questions (Reading & Writing)."""
from __future__ import annotations
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ingestion.embed import embed_batch
from ingestion.load import get_collection

QUESTIONS = [
    {
        "id": "72df7623",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In 2018 researchers Adwait Deshpande, Shreejata Gupta, and Anindya Sinha were observing wild macaques in India's Bandipur National Park.\n"
            "• They saw macaques calling out to and gesturing at humans who were eating or carrying food.\n"
            "• They designed a study to find out if the macaques were intentionally communicating to try to persuade the humans to share their food.\n"
            "• In the study trials, macaques frequently called out to and gestured at humans holding food.\n"
            "• In the study trials, macaques called out to and gestured at empty-handed humans less frequently.\n\n"
            "The student wants to present the study's results. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Macaques in the study called out to and gestured more frequently at humans holding food than at empty-handed humans.",
            "B) In 2018, researchers who had observed macaques in India's Bandipur National Park calling out to and gesturing at humans designed a study.",
            "C) The researchers hoped to find out if the macaques were intentionally communicating to try to persuade humans to share their food.",
            "D) The researchers studied how macaques behaved around both humans holding food and empty-handed humans.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A presents the study's results from the last two bullet points. Choice B describes the background and motivation of the study but not the outcome. Choice C describes the research question or hypothesis but not the evidence or conclusion. Choice D describes the method or design of the study but not the actual results.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "10af0d71",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• A marathon is a long-distance running race that is 26.2 miles long.\n"
            "• An ultramarathon is a long-distance running race of more than 26.2 miles.\n"
            "• The Kepler Challenge is a one-day, 37.3-mile ultramarathon in New Zealand.\n"
            "• The Spreelauf is a six-day, 261-mile ultramarathon in Germany.\n\n"
            "The student wants to make a generalization about ultramarathons. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Examples of ultramarathons include the 37.3-mile Kepler Challenge in New Zealand and the 261-mile Spreelauf in Germany.",
            "B) A marathon is 26.2 miles long, but the Spreelauf ultramarathon, at 261 miles, is far longer.",
            "C) Ultramarathons range widely in length, from a few dozen miles to a few hundred.",
            "D) While the Kepler Challenge is a one-day ultramarathon, the Spreelauf is a six-day ultramarathon.",
        ],
        "correct_answer": "C",
        "explanation": "Choice C is the only choice that makes a generalization about ultramarathons as a category. Choice A gives specific examples but doesn't generalize. Choice B compares marathons to one specific ultramarathon without generalizing about the category. Choice D contrasts two specific ultramarathons without making a broader claim.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "0314684f",
        "question_text": (
            "Alexander Lawrence Posey (1873–1908) varied his focus and tone depending on the genre in which he was writing. "
            "In his poetry, he used heartfelt language to evoke the beauty and peacefulness of his natural surroundings; in his journalism, "
            "______ he employed humor and satire to comment on political issues affecting his Muskogee Creek community.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) that is,",
            "B) granted,",
            "C) similarly,",
            "D) by contrast,",
        ],
        "correct_answer": "D",
        "explanation": '"By contrast" fits because the text contrasts Posey\'s heartfelt tone in poetry with the humor and satire of his journalism. Choice A (that is) indicates restatement, not contrast. Choice B (granted) means admittedly, but the text isn\'t conceding anything. Choice C (similarly) indicates an agreeing idea, but the two examples are intentionally very different.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "108fb9e7",
        "question_text": (
            "“Wishcycling”—putting nonrecyclable items into recycling bins under the mistaken belief that those items can be recycled—"
            "ultimately does more harm than good. Nonrecyclable items, such as greasy pizza boxes, can contaminate recyclable materials, "
            "rendering entire batches unusable. ______ nonrecyclable products can damage recycling plants’ machinery.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) Fittingly,",
            "B) On the contrary,",
            "C) Moreover,",
            "D) Nevertheless,",
        ],
        "correct_answer": "C",
        "explanation": '"Moreover" fits because this sentence adds another supporting example of how wishcycling is harmful. Choice A (fittingly) means "appropriately," which doesn\'t fit. Choices B and D (on the contrary, nevertheless) are disagreement transitions, but this sentence agrees with the previous one.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "2e543111",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Generally, an object will heat up when twisted.\n"
            "• The twisting of an object is known as torsion.\n"
            "• A 2019 study led by Zunfeng Liu and Ray Baughman tested the torsional heating of various fibers.\n"
            "• When a 3-millimeter-thick sample of thermoplastic polyurethane (TPU) fiber was twisted, its average surface temperature increased by 6°C.\n"
            "• When a 4-millimeter-thick sample of styrene-ethylene-butylene-styrene (SEBS) rubber fiber was twisted, its average surface temperature increased by 3.5°C.\n\n"
            "The student wants to contrast the two samples. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) When the fibers were twisted as part of the 2019 study, the surface temperature of both samples increased.",
            "B) In 2019, researchers studied the effect of torsional heating on various fibers, including samples of SEBS rubber and TPU.",
            "C) Twisting an object will generally cause its temperature to increase, a process known as torsional heating.",
            "D) The SEBS rubber sample used in the 2019 study was thicker than the TPU sample.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D contrasts the two samples by noting the SEBS rubber sample (4mm) was thicker than the TPU sample (3mm). Choice A mentions a similarity (both temperatures increased), not a contrast. Choice B indicates both were part of the study without contrasting them. Choice C describes torsional heating generally without contrasting the samples.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "f65de8d2",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Muckrakers were journalists who sought to expose corruption in US institutions during the Progressive Era (1897–1920).\n"
            "• Ida Tarbell was a muckraker who investigated the Standard Oil Company.\n"
            "• She interviewed Standard Oil Company executives, oil industry workers, and public officials.\n"
            "• She examined thousands of pages of the company’s internal communications, including letters and financial records.\n"
            "• Her book The History of the Standard Oil Company (1904) exposed the company’s unfair business practices.\n\n"
            "The student wants to emphasize the thoroughness of Ida Tarbell’s investigation of the Standard Oil Company. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Ida Tarbell not only interviewed Standard Oil executives, oil industry workers, and public officials but also examined thousands of pages of the company’s internal communications.",
            "B) Ida Tarbell, who investigated the Standard Oil Company, was a muckraker (a journalist who sought to expose corruption in US institutions during the Progressive Era, 1897–1920).",
            "C) As part of her investigation of the Standard Oil Company, muckraker Ida Tarbell conducted interviews.",
            "D) Published in 1904, muckraker Ida Tarbell’s book The History of the Standard Oil Company exposed the company’s unfair business practices.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A emphasizes thoroughness by describing both the breadth of interviews and examination of thousands of pages of internal communications. Choice B gives a biographical sketch without emphasizing thoroughness. Choice C only mentions interviews, omitting the examination of records. Choice D describes her book rather than the investigation itself.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "43ca2315",
        "question_text": (
            "To discover which fruit varieties were grown in Italy’s Umbria region before the introduction of industrial farming, "
            "botanist Isabella Dalla Ragione often turns to centuries-old lists of cooking ingredients. "
            "______ she analyzes Renaissance paintings of Umbria, as they can provide accurate representations of fruits that were grown there long ago.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) In sum,",
            "B) Instead,",
            "C) Thus,",
            "D) Additionally,",
        ],
        "correct_answer": "D",
        "explanation": '"Additionally" signals that the painting analysis is an additional research method, not a replacement or result. Choice A (in sum) implies a concluding summary. Choice B (instead) implies an alternative to looking at ingredient lists. Choice C (thus) implies the painting analysis results from the ingredient list research.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "88c4086d",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Tecozautla is a municipality in the state of Hidalgo, Mexico.\n"
            "• Municipalities are governmental regions responsible for providing many public services to their residents.\n"
            "• One service they provide is street lighting.\n"
            "• Tecozautla covers an area of roughly 535 km².\n"
            "• Hidalgo is divided into 84 municipalities.\n\n"
            "The student wants to emphasize the size of Tecozautla. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) The municipality of Tecozautla in Hidalgo, Mexico, covers an area of roughly 535 km².",
            "B) Providing street lighting is just one example of the public services that municipalities provide.",
            "C) Tecozautla is one of 84 governmental regions, known as municipalities, across Hidalgo.",
            "D) Tecozautla—a governmental region in the state of Hidalgo, Mexico—provides many public services to its residents.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A directly emphasizes Tecozautla's size (roughly 535 km²). Choice B discusses public services, not size. Choice C provides Tecozautla's count among municipalities but not its actual area. Choice D describes its governmental role but not its size.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "3ba08ce1",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Maikaʻi Tubbs is a Native Hawaiian sculptor and installation artist.\n"
            "• His work has been shown in the United States, Canada, Japan, and Germany, among other places.\n"
            "• Many of his sculptures feature discarded objects.\n"
            "• His work Erasure (2008) includes discarded audiocassette tapes and magnets.\n"
            "• His work Home Grown (2009) includes discarded pushpins, plastic plates and forks, and wood.\n\n"
            "The student wants to emphasize a similarity between the two works. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Erasure (2008) uses discarded objects such as audiocassette tapes and magnets; Home Grown (2009), however, includes pushpins, plastic plates and forks, and wood.",
            "B) Tubbs’s work, which often features discarded objects, has been shown both within the United States and abroad.",
            "C) Like many of Tubbs’s sculptures, both Erasure and Home Grown include discarded objects: Erasure uses audiocassette tapes, and Home Grown uses plastic forks.",
            "D) Tubbs completed Erasure in 2008 and Home Grown in 2009.",
        ],
        "correct_answer": "C",
        "explanation": 'Choice C emphasizes a similarity by identifying a shared trait: both Erasure and Home Grown include discarded objects. Choice A uses "however," emphasizing differences in materials. Choice B mentions Tubbs\'s work broadly without detailing the two specific works. Choice D only shows the works were completed at different times.',
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "6800c1cc",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Cecilia Vicuña is a multidisciplinary artist.\n"
            "• In 1971, her first solo art exhibition, Pinturas, poemas y explicaciones, was shown at the Museo Nacional de Bellas Artes in Santiago, Chile.\n"
            "• Her poetry collection Precario/Precarious was published in 1983 by Tanam Press.\n"
            "• Her poetry collection Instan was published in 2002 by Kelsey St. Press.\n"
            "• She lives part time in Chile, where she was born, and part time in New York.\n\n"
            "The student wants to introduce the artist’s 1983 poetry collection. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Before she published the books Precario/Precarious (1983) and Instan (2002), Cecilia Vicuña exhibited visual art at the Museo Nacional de Bellas Artes in Santiago, Chile.",
            "B) Cecilia Vicuña is a true multidisciplinary artist whose works include numerous poetry collections and visual art exhibitions.",
            "C) Published in 1983 by Tanam Press, Precario/Precarious is a collection of poetry by the multidisciplinary artist Cecilia Vicuña.",
            "D) In 1971, Cecilia Vicuña exhibited her first solo art exhibition, Pinturas, poemas y explicaciones, in Chile, her country of birth.",
        ],
        "correct_answer": "C",
        "explanation": "Choice C effectively introduces the 1983 poetry collection Precario/Precarious, noting it's by Vicuña and was published by Tanam Press. Choice A mentions the collection but focuses on visual art. Choice B introduces Vicuña herself, not the specific collection. Choice D emphasizes the 1971 exhibition, not the 1983 collection.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "a846cda0",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In the early 1960s, the US had a strict national-origins quota system for immigrants.\n"
            "• The number of new immigrants allowed from a country each year was based on how many people from that country lived in the US in 1890.\n"
            "• This system favored immigrants from northern Europe.\n"
            "• Almost 70% of slots were reserved for immigrants from Great Britain, Ireland, and Germany.\n"
            "• The 1965 Hart-Celler Act abolished the national-origins quota system.\n\n"
            "The student wants to present the significance of the Hart-Celler Act to an audience unfamiliar with the history of US immigration. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Almost 70% of slots were reserved for immigrants from Great Britain, Ireland, and Germany at the time the Hart-Celler Act was proposed.",
            "B) Prior to the Hart-Celler Act, new immigration quotas were based on how many people from each country lived in the US in 1890.",
            "C) The quota system in place in the early 1960s was abolished by the 1965 Hart-Celler Act.",
            "D) The 1965 Hart-Celler Act abolished the national-origins quota system, which favored immigrants from northern Europe.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D presents the Hart-Celler Act's significance to an unfamiliar audience — noting it abolished the national-origins quota system and explaining why that mattered (the system favored northern Europeans). Choice A describes one aspect of the old policy without the act's significance. Choice B describes prior policy without the act itself. Choice C states the act abolished the system but doesn't explain either to an unfamiliar audience.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "e162b5ae",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Texture analysis and historical analysis are two approaches to art criticism.\n"
            "• Texture analysis examines how surfaces are visually represented in an artwork.\n"
            "• Such an analysis of Giorgione’s Youth Holding an Arrow might consider how the painting’s blended colors make the subject’s skin appear smooth in texture.\n"
            "• Historical analysis considers the historical context in which a work was created.\n"
            "• Such an analysis of Diego Velázquez’s Las Meninas might consider how the painting’s depiction of the artist with King Philip IV symbolizes art’s historical ties to power.\n\n"
            "The student wants to present historical analysis to an audience unfamiliar with the concept. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) A texture analysis of Youth Holding an Arrow might consider how the painting’s blended colors make the subject’s skin appear smooth in texture.",
            "B) Texture analysis differs from historical analysis in that texture analysis examines how surfaces are visually represented in an artwork.",
            "C) An approach to art criticism, historical analysis considers the historical context in which a work was created.",
            "D) Las Meninas’s depiction of the artist with King Philip IV symbolizes art’s historical ties to power.",
        ],
        "correct_answer": "C",
        "explanation": "Choice C presents historical analysis to an unfamiliar audience by defining it as an approach to art criticism that considers historical context. Choice A provides an example of texture analysis, not historical analysis. Choice B explains a difference between the two approaches without defining historical analysis. Choice D gives an example of historical analysis without defining the concept.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "d305b5c4",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In 1999, astronomer Todd Henry studied the differences in surface temperature between the Sun and nearby stars.\n"
            "• His team mapped all stars within 10 parsecs (approximately 200 trillion miles) of the Sun.\n"
            "• The surface temperature of the Sun is around 9,800°F, which classifies it as a G star.\n"
            "• 327 of the 357 stars in the study were classified as K or M stars, with surface temperatures under 8,900°F (cooler than the Sun).\n"
            "• 11 of the 357 stars in the study were classified as A or F stars, with surface temperatures greater than 10,300°F (hotter than the Sun).\n\n"
            "The student wants to emphasize how hot the Sun is relative to nearby stars. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) At around 9,800°F, which classifies it as a G star, the Sun is hotter than most but not all of the stars within 10 parsecs of it.",
            "B) Astronomer Todd Henry determined that the Sun, at around 9,800°F, is a G star, and several other stars within a 10-parsec range are A or F stars.",
            "C) Of the 357 stars within ten parsecs of the Sun, 327 are classified as K or M stars, with surface temperatures under 8,900°F.",
            "D) While most of the stars within 10 parsecs of the Sun are classified as K, M, A, or F stars, the Sun is classified as a G star due to its surface temperature of 9,800°F.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A emphasizes how hot the Sun is relative to nearby stars — it's hotter than most (327 K/M stars) but not all (11 A/F stars). Choice B doesn't directly compare the Sun's heat to nearby stars. Choice C discusses nearby cooler stars without mentioning the Sun's relative position. Choice D notes the Sun is classified differently but doesn't emphasize how hot it is relative to nearby stars.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "cdb5fb80",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Etel Adnan was a Lebanese American poet and artist known for making many leporellos.\n"
            "• A leporello is an artist’s book that is folded accordion style.\n"
            "• When the book is expanded, the artist’s work is revealed, and its zigzag shape allows it to stand on its own.\n"
            "• Her leporello December from My Window (1993) features a panoramic landscape.\n"
            "• It is painted using ink and watercolor.\n\n"
            "The student wants to describe Adnan’s December from My Window to an audience already familiar with leporellos. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Featuring a panoramic landscape, the 1993 work is one of Adnan’s many leporellos, which are accordion-style folded books that when expanded reveal the artist’s work.",
            "B) When expanded, Adnan’s 1993 leporello December from My Window reveals a panoramic landscape painted in ink and watercolor.",
            "C) Known for making many other accordion-style folded books called leporellos, Adnan created December from My Window in 1993.",
            "D) A leporello, such as Adnan’s December from My Window, is folded accordion style, and due to its zigzag shape it is able to stand on its own when fully expanded.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B describes the work assuming the audience already knows what a leporello is, focusing on its content (panoramic landscape) and medium (ink and watercolor). Choice A unnecessarily defines leporellos for an already-familiar audience. Choice C doesn't describe the content or medium and also defines leporellos. Choice D defines leporellos, which is unnecessary for a familiar audience.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "95db4b9e",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Gravitational waves are powerful ripples that originate in deep space and eventually pass through Earth.\n"
            "• The Laser Interferometer Gravitational Wave Observatory (LIGO) is a physics study that began in 2002.\n"
            "• LIGO’s goal is to detect and analyze gravitational waves.\n"
            "• LIGO uses a pair of massive gravitational wave detectors called interferometers that are thousands of miles apart.\n"
            "• In 2015, for the first time in history, LIGO researchers detected a gravitational wave passing through Earth.\n\n"
            "The student wants to present LIGO’s aim and methodology. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) In 2015, LIGO’s massive interferometers detected a powerful ripple that originated in deep space and eventually passed through Earth.",
            "B) Though the physics study LIGO began in 2002, its massive interferometers didn’t detect a gravitational wave until 2015.",
            "C) To achieve its aims, LIGO uses a pair of massive interferometers that are thousands of miles apart.",
            "D) A physics study designed to detect and analyze gravitational waves, LIGO uses a pair of massive interferometers that are thousands of miles apart.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D presents both LIGO's aim (to detect and analyze gravitational waves) and methodology (a pair of massive interferometers thousands of miles apart). Choice A describes a finding, not the aim or methodology. Choice B provides timeline background, not the aim or methodology. Choice C touches on methodology but doesn't state LIGO's aims.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "355d0918",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Some US reformers sought to improve society in the 1800s by building utopias.\n"
            "• A utopia is a community intended to represent a perfect society based on a specific set of principles.\n"
            "• One such community was Brook Farm near Boston, Massachusetts.\n"
            "• It was founded in 1841 by writer George Ripley.\n"
            "• Ripley wrote in a letter that his goal for Brook Farm was “to guarantee the highest mental freedom, by providing all with labor, adapted to their tastes and talents, and securing to them the fruits of their industry.”\n\n"
            "The student wants to explain the goal of Brook Farm using a quotation from George Ripley. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) In a letter, writer George Ripley explained his goal to “guarantee the highest mental freedom.”",
            "B) Utopias, such as Brook Farm, founded by George Ripley in 1841, were based on a specific set of principles intended to create a perfect society.",
            "C) Founded by George Ripley near Boston, Massachusetts, Brook Farm was part of a trend in the 1800s, when reformers in the United States built utopias.",
            "D) Established in 1841, Brook Farm was a utopian community created to “guarantee the highest mental freedom, by providing all with labor... [and] the fruits of their industry,” according to founder George Ripley.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D explains the goal of Brook Farm using a quotation from Ripley. Choice A uses only part of Ripley's goal and doesn't mention Brook Farm. Choice B defines utopia but doesn't use Ripley's words to describe his vision. Choice C provides background about Brook Farm but doesn't explain its goals or include Ripley's words.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "c88233b4",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Chromosomes are cellular structures that contain genes.\n"
            "• Genes carry critical instructions for determining an organism’s physical traits.\n"
            "• Members of the same species typically have the same number of chromosomes.\n"
            "• The pineapple (Ananas comosus) and the melon (Cucumis melo) are species of fruits.\n"
            "• The pineapple has fifty chromosomes.\n"
            "• The melon has twenty-four chromosomes.\n\n"
            "The student wants to specify how many chromosomes the pineapple has. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) The pineapple’s chromosomes contain genes, which are critical to determining an organism’s physical traits.",
            "B) The pineapple (Ananas comosus) has fifty chromosomes.",
            "C) The pineapple (Ananas comosus) and the melon (Cucumis melo) both have chromosomes, but the pineapple has more than the melon does.",
            "D) The melon, a species of fruit, has twenty-four structures called chromosomes.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B directly specifies how many chromosomes the pineapple has: fifty. Choice A mentions the pineapple's chromosomes but doesn't specify the number. Choice C says the pineapple has more than the melon but doesn't give the exact number. Choice D specifies the melon's count, not the pineapple's.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "69281ab2",
        "question_text": (
            "In a 2022 analysis of 200 terms, researchers found a broad pattern of valence-dependent mutation for which negative words saw "
            "a faster rate of cognate replacement—______ the rate at which a word will be replaced over time with a noncognate form. "
            "Adjectives (e.g., “afraid”) saw the largest effect; nouns (e.g., “attack”), meanwhile, saw the smallest.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) for example,",
            "B) likewise,",
            "C) in addition,",
            "D) that is,",
        ],
        "correct_answer": "D",
        "explanation": '"That is" signals that the following information clarifies the term cognate replacement, defined just before it. Choice A (for example) implies what follows provides a specific example of the findings. Choice B (likewise) implies similarity to prior information. Choice C (in addition) implies the following merely adds to prior information.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "6fb1f442",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In the late 1890s, over 14,000 unique varieties of apples were grown in the US.\n"
            "• The rise of industrial agriculture in the mid-1900s narrowed the range of commercially grown crops.\n"
            "• Thousands of apple varieties considered less suitable for commercial growth were lost.\n"
            "• Today, only 15 apple varieties dominate the market, making up 90% of apples purchased in the US.\n"
            "• The Lost Apple Project, based in Washington State, attempts to find and grow lost apple varieties.\n\n"
            "The student wants to emphasize the decline in unique apple varieties in the US and specify why this decline occurred. Which choice most effectively uses relevant information from the notes to accomplish these goals?"
        ),
        "choices": [
            "A) The Lost Apple Project is dedicated to finding some of the apple varieties lost following a shift in agricultural practices in the mid-1900s.",
            "B) While over 14,000 apple varieties were grown in the US in the late 1890s, only 15 unique varieties make up most of the apples sold today.",
            "C) Since the rise of industrial agriculture, US farmers have mainly grown the same few unique apple varieties, resulting in the loss of thousands of varieties less suitable for commercial growth.",
            "D) As industrial agriculture rose to prominence in the mid-1900s, the number of crops selected for cultivation decreased dramatically.",
        ],
        "correct_answer": "C",
        "explanation": "Choice C both emphasizes the decline and specifies why it occurred — the rise of industrial agriculture caused farmers to mainly grow the same few varieties, losing thousands of others. Choice A introduces the Lost Apple Project without addressing both goals. Choice B emphasizes the decline but not the cause. Choice D emphasizes the general decline of crops without focusing specifically on apple varieties.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "5e3e20f9",
        "question_text": (
            "For years, biologists have experimented with using grime-eating bacteria rather than harsh chemicals to clean artworks, "
            "and results have been impressive overall. ______ these bacterial strains—which can metabolize centuries’ worth of oil, glue, dirt, "
            "and other surface impurities without creating harmful byproducts—have proven more effective than traditional chemical cleaning methods.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) However,",
            "B) In many cases,",
            "C) As a result,",
            "D) Additionally,",
        ],
        "correct_answer": "B",
        "explanation": '"In many cases" fits because this sentence elaborates on the "impressive results" with specific details — not a new idea but elaboration on the same point. Choice A (however) is a disagreement transition, but this sentence agrees with the previous. Choice C (as a result) implies cause-and-effect that doesn\'t fit. Choice D (additionally) introduces a new idea, but this sentence elaborates on the existing claim.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "c32f7659",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Sam Maloof (1916–2009) was an American woodworker and furniture designer.\n"
            "• He was the son of Lebanese immigrants.\n"
            "• He received a “genius grant” from the John D. and Catherine T. MacArthur Foundation in 1985.\n"
            "• The Museum of Fine Arts in Boston, Massachusetts, owns a rocking chair that Maloof made from walnut wood.\n"
            "• The armrests and the seat of the chair are sleek and contoured, and the back consists of seven spindle-like slats.\n\n"
            "The student wants to describe the rocking chair to an audience unfamiliar with Sam Maloof. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) With its sleek, contoured armrests and seat, the walnut rocking chair in Boston’s Museum of Fine Arts is just one piece of furniture created by American woodworker Sam Maloof.",
            "B) Sam Maloof was born in 1916 and died in 2009, and during his life, he made a chair that you can see if you visit the Museum of Fine Arts in Boston.",
            "C) Furniture designer Sam Maloof was a recipient of one of the John D. and Catherine T. MacArthur Foundation’s “genius grants.”",
            "D) The rocking chair is made from walnut, and it has been shaped such that its armrests and seat are sleek and contoured.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A describes the rocking chair to an unfamiliar audience — noting its sleek, contoured armrests and seat, and identifying Maloof as an American woodworker. Choice B explains who Maloof was but doesn't describe the chair. Choice C identifies Maloof but doesn't describe the chair. Choice D describes the chair but doesn't explain who Sam Maloof was.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "fbb716d4",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Hina Hanta is an online archive curated by the Choctaw Nation of Oklahoma.\n"
            '• Hina Hanta means “bright path” in Choctaw.\n'
            "• It features images of cultural artifacts relevant to the history of the Choctaw people.\n"
            "• It includes a fanner basket (ufko tapushik in Choctaw) made from cane.\n"
            "• It includes a robe (nita anchi) made from bear fur.\n\n"
            "The student wants to specify the fanner basket’s name in Choctaw. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) The Hina Hanta archive features cultural artifacts, such as a fanner basket and a robe, that are relevant to the history of the Choctaw people.",
            "B) The cane fanner basket, which is included in the Hina Hanta online archive, is called an ufko tapushik in Choctaw.",
            'C) Hina Hanta, which means “bright path” in Choctaw, includes a fanner basket in its archive.',
            'D) The name of the online archive Hina Hanta means “bright path” in Choctaw.',
        ],
        "correct_answer": "B",
        "explanation": "Choice B specifies the fanner basket's Choctaw name (ufko tapushik). Choice A mentions the fanner basket but not its Choctaw name. Choice C mentions the fanner basket but not its Choctaw name. Choice D doesn't mention the fanner basket at all.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "d52ab835",
        "question_text": (
            "When, in the 1800s, geologists first realized that much of Earth had once been covered by great sheets of ice, some theorized that "
            "the phenomenon was cyclical, occurring at regular intervals. Each Ice Age is so destructive, though, that it largely erases the "
            "geological evidence of its predecessor. ______ geologists were unable to confirm the theory of cyclical Ice Ages until the 1960s.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) Hence,",
            "B) Moreover,",
            "C) Nevertheless,",
            "D) Next,",
        ],
        "correct_answer": "A",
        "explanation": '"Hence" signals that geologists being unable to confirm the theory is a consequence of Ice Ages erasing geological evidence. Choice B (moreover) signals additional information rather than a consequence. Choice C (nevertheless) is a disagreement transition, but this sentence follows logically from the previous. Choice D (next) signals a sequential step rather than a consequence.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "c6783904",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Lighthouses send out crucial light signals to help ships and other watercraft navigate at night.\n"
            "• Before automation, lighthouses were run by lighthouse keepers.\n"
            "• Maria Younghans was the lighthouse keeper at Biloxi Light in Mississippi.\n"
            "• She held this position from 1867 to 1918.\n"
            "• Flora McNeil was the lighthouse keeper at Bridgeport Breakwater Light in Connecticut.\n"
            "• She held this position from 1904 to 1920.\n\n"
            "The student wants to emphasize the order in which the two lighthouse keepers began their careers. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) From 1867 to 1918, the nighttime waters of Mississippi were more navigable thanks to lighthouse keepers Flora McNeil and Maria Younghans.",
            "B) Before automation, lighthouse keepers like Maria Younghans and Flora McNeil were crucial to ensuring safe navigation for watercraft.",
            "C) Flora McNeil began her career as a lighthouse keeper years after Maria Younghans did.",
            "D) Maria Younghans’s career as a lighthouse keeper ended in 1918, whereas Flora McNeil’s ended in 1920.",
        ],
        "correct_answer": "C",
        "explanation": "Choice C emphasizes when each keeper began — McNeil (1904) started years after Younghans (1867). Choice A makes a generalization about navigable waters and misrepresents information. Choice B claims they were crucial without emphasizing the order they began. Choice D emphasizes when their careers ended, not when they began.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "bffa7aea",
        "question_text": (
            "Establishing Coordinated Universal Time (UTC) is no easy task. Each month, readings of a single second from atomic clocks "
            "around the world are taken and sent to the International Bureau of Weights and Measures (BIPM) in France. "
            "______ BIPM metrologists perform the meticulous work of assembling these minutely disparate readings into a globally shared time standard.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) There,",
            "B) In particular,",
            "C) For example,",
            "D) Conversely,",
        ],
        "correct_answer": "A",
        "explanation": '"There" indicates the meticulous work takes place at the BIPM in France — a locative transition fitting the context. Choices B and C (in particular, for example) are exemplification transitions that don\'t fit since this sentence describes where the work happens, not an example. Choice D (conversely) is a disagreement transition, but this sentence doesn\'t contradict the previous one.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "40f0633c",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Pineapple is a fruit that contains ascorbic acid, an essential nutrient for humans.\n"
            "• Every 100 grams (g) of pineapple contains 48 milligrams (mg) of ascorbic acid.\n"
            "• Many animals can make ascorbic acid in their bodies, but humans cannot.\n"
            "• Humans must get ascorbic acid from foods, including fruits and vegetables.\n"
            "• Ascorbic acid is also known as vitamin C.\n\n"
            "The student wants to provide an example of a fruit that contains vitamin C. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Humans cannot make ascorbic acid in their bodies, but they can get it from foods, such as fruits, for example.",
            "B) Vitamin C, also known as ascorbic acid, can be found in pineapple as well as other fruits.",
            "C) Since humans cannot make vitamin C in their bodies, they must get it from food.",
            "D) Many animals can make ascorbic acid, which is also known as vitamin C, in their bodies, but humans cannot.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B provides a specific example of a fruit (pineapple) that contains vitamin C. Choice A explains humans can get vitamin C from fruits without naming a specific fruit. Choice C explains why humans need to get it from food without naming a specific fruit. Choice D compares production in animals vs. humans without providing a fruit example.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "8412b266",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Grimanesa Amoros is a Peruvian American artist well known for her LED light sculptures.\n"
            "• Her sculpture Uros Island is made of smooth multicolored LED domes.\n"
            "• It occupies 335 cubic feet of space.\n"
            "• Her sculpture Fortuna is made of entangled blue and white LED tubes.\n"
            "• It occupies 19,950 cubic feet of space.\n\n"
            "The student wants to emphasize a similarity between Uros Island and Fortuna. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) The smooth LED domes of Grimanesa Amoros’s Uros Island stand in contrast to the tangled LED tubes of Fortuna.",
            "B) At 19,950 cubic feet in size, Grimanesa Amoros’s Fortuna cuts a larger figure than the 335-cubic-foot Uros Island.",
            "C) Grimanesa Amoros is the artist behind Uros Island—a sculpture made of smooth multicolored LED domes.",
            "D) Uros Island is an LED light sculpture made by Grimanesa Amoros, as is Fortuna.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D emphasizes a similarity — both Uros Island and Fortuna are LED light sculptures created by Grimanesa Amoros. Choice A uses 'in contrast,' emphasizing a difference. Choice B contrasts their sizes — a difference, not a similarity. Choice C only describes Uros Island without mentioning Fortuna.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "68ef9df3",
        "question_text": (
            "Jhumpa Lahiri’s story collection Interpreter of Maladies features multiple stories about romantic relationships. "
            "In “This Blessed House,” newlyweds argue over whether to replace items left by the previous owners of their new home. "
            "______ in “A Temporary Matter,” a husband and wife attempt to rekindle their relationship during a four-night blackout.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) Granted,",
            "B) For example,",
            "C) Likewise,",
            "D) Hence,",
        ],
        "correct_answer": "C",
        "explanation": '"Likewise" indicates the addition of a new but related idea — another story about romantic relationships dealing with challenges. Choice A (granted) means admittedly, but the text isn\'t conceding anything. Choice B (for example) implies the second story is an example of the first story. Choice D (hence) implies cause-and-effect — the first story didn\'t cause the second.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "fbb64b41",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Claude McKay (1889–1948) was a Jamaican American writer.\n"
            "• Songs of Jamaica (1912) and Constab Ballads (1912) are two acclaimed poetry collections that McKay published while living in Jamaica.\n"
            "• McKay moved to Harlem in New York City in 1914.\n"
            "• He is best known as a poet and novelist of the Harlem Renaissance, a literary and cultural movement of the 1920s and 1930s.\n"
            "• His most famous works include the poetry collection Harlem Shadows (1922) and the novel Home to Harlem (1928).\n\n"
            "The student wants to emphasize Claude McKay’s accomplishments before moving to Harlem. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Jamaican American writer Claude McKay is the author of works such as Songs of Jamaica (1912), Constab Ballads (1912), Harlem Shadows (1922), and Home to Harlem (1928).",
            "B) Although he is best known as a Harlem Renaissance writer, Claude McKay had published two acclaimed poetry collections in 1912 while living in Jamaica: Songs of Jamaica and Constab Ballads.",
            "C) In 1914, Claude McKay moved to Harlem, where he would become known as a poet and novelist of the Harlem Renaissance (a literary and cultural movement of the 1920s and 1930s).",
            "D) Before moving to Harlem, Claude McKay—author of the poetry collection Harlem Shadows (1922) and the novel Home to Harlem (1928)—lived in Jamaica.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B contrasts McKay's Harlem Renaissance fame with his earlier Jamaican achievements and names the two pre-Harlem collections. Choice A lists works from both periods without distinguishing pre-Harlem from post-Harlem. Choice C only mentions his move and what he became known for afterward. Choice D mentions he lived in Jamaica but doesn't name the works he published there.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "6b646bda",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Marine biologist Camille Jazmin Gaynus studies coral reefs.\n"
            "• Coral reefs are vital underwater ecosystems that provide habitats to 25% of all marine species.\n"
            "• Reefs can include up to 8,000 species of fish, such as toadfish, seahorses, and clown triggerfish.\n"
            "• The Amazon Reef is a coral reef in Brazil.\n"
            "• It is one of the largest known reefs in the world.\n\n"
            "The student wants to introduce the scientist and her field of study to a new audience. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Located in Brazil, the Amazon Reef is one of the largest known coral reefs in the world.",
            "B) Marine biologist Camille Jazmin Gaynus studies coral reefs, vital underwater ecosystems that provide homes to 25% of all marine species.",
            "C) Providing homes to 25% of all marine species, including up to 8,000 species of fish, coral reefs are vital underwater ecosystems and thus of great interest to marine biologists.",
            "D) As Camille Jazmin Gaynus knows well, coral reefs are vital underwater ecosystems, providing homes to thousands of species of fish.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B introduces the scientist (marine biologist Camille Jazmin Gaynus) and her field of study (coral reefs). Choice A doesn't mention Gaynus at all. Choice C doesn't mention Gaynus at all. Choice D mentions Gaynus but doesn't identify her as a marine biologist or establish her field of study.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "51f975cc",
        "question_text": (
            "Scientists were able to isolate a relatively pure sample of selenium in 1817, the same year they first discovered the element’s existence. "
            "______ the isolation process took longer for molybdenum, which was isolated in its pure form three years after scientists first discovered it.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) By contrast,",
            "B) Thus,",
            "C) Similarly,",
            "D) For instance,",
        ],
        "correct_answer": "A",
        "explanation": '"By contrast" signals that molybdenum\'s isolation took longer — contrasting with selenium\'s same-year isolation. Choice B (thus) implies cause-and-effect. Choice C (similarly) implies the experiences were similar, but molybdenum took longer, which is the opposite. Choice D (for instance) implies molybdenum exemplifies selenium\'s short process.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "68609a2d",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Soo Sunny Park is a Korean American artist who uses light as her primary medium of expression.\n"
            "• She created her work Unwoven Light in 2013.\n"
            "• Unwoven Light featured a chain-link fence fitted with iridescent plexiglass tiles.\n"
            "• When light passed through the fence, colorful prisms formed.\n\n"
            "The student wants to describe Unwoven Light to an audience unfamiliar with Soo Sunny Park. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Park’s 2013 installation Unwoven Light, which included a chain-link fence and iridescent tiles made from plexiglass, featured light as its primary medium of expression.",
            "B) Korean American light artist Soo Sunny Park created Unwoven Light in 2013.",
            "C) The chain-link fence in Soo Sunny Park’s Unwoven Light was fitted with tiles made from iridescent plexiglass.",
            "D) In Unwoven Light, a 2013 work by Korean American artist Soo Sunny Park, light formed colorful prisms as it passed through a fence Park had fitted with iridescent tiles.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D describes Unwoven Light to an unfamiliar audience — noting Park's identity (Korean American artist) and the work's key details (colorful prisms from light through iridescent tiles). Choice A describes the work but doesn't introduce who Park is. Choice B introduces Park but lacks descriptive details about the work. Choice C mentions Park and one aspect of the work but doesn't effectively describe the overall piece.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "8bd3381f",
        "question_text": (
            "With their distinctive cone shapes and steeply sloping sides, the volcanoes Hverfjall (Iceland) and Toliman (Guatemala) may look "
            "similar from afar. Tehnuka Ilanko and other volcanologists, ______ can tell by how each was formed that Hverfjall is a cinder cone "
            "volcano, while Toliman is a composite volcano.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) for example,",
            "B) in addition,",
            "C) therefore,",
            "D) though,",
        ],
        "correct_answer": "D",
        "explanation": '"Though" qualifies the apparent similarity — the volcanoes look similar but volcanologists can distinguish them as two different types. Choice A (for example) implies this exemplifies the previous information about similarity. Choice B (in addition) merely adds to the previous information. Choice C (therefore) implies cause-and-effect from the volcanoes looking similar.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "aadcdfa3",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In geology, an Aeolian landform is one that has been created by the wind.\n"
            "• In Greek mythology, Aeolus is the keeper of the winds.\n"
            "• Aeolian landforms are created when the wind erodes, transports, or deposits material.\n"
            "• A mushroom rock is a rock formation in which the top is wider than the base.\n"
            "• A mushroom rock can be formed when the wind erodes the base and the top at different rates.\n\n"
            "The student wants to provide an explanation and an example of Aeolian landforms. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Aeolian landforms are created by different wind-based processes; for example, some are created by wind erosion.",
            "B) Aeolian landforms—landforms created by the wind—include the mushroom rock, a rock formation in which the wind erodes the base of the rock faster than the top.",
            "C) Erosion, transportation, and deposition are three examples of how the wind can create Aeolian landforms and mushroom rocks.",
            "D) A mushroom rock is a rock formation that owes its shape to the wind, a natural force associated with Aeolus in Greek mythology.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B provides both an explanation (Aeolian landforms are created by wind) and a specific example (the mushroom rock, including how wind erosion forms it). Choice A explains Aeolian landforms but gives an example of a wind-based process rather than a landform. Choice C doesn't effectively provide a landform example. Choice D explains the mushroom rock specifically without explaining Aeolian landforms generally.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "99c3a1db",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Organisms release cellular material into their environment by shedding substances such as hair or skin.\n"
            "• The DNA in these substances is known as environmental DNA, or eDNA.\n"
            "• Researchers collect and analyze eDNA to detect the presence of species that are difficult to observe.\n"
            "• Geneticist Sara Oyler-McCance’s research team analyzed eDNA in water samples from the Florida Everglades to detect invasive constrictor snake species in the area.\n"
            "• The study determined a 91% probability of detecting Burmese python eDNA in a given location.\n\n"
            "The student wants to present the study to an audience already familiar with environmental DNA. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Sara Oyler-McCance’s researchers analyzed eDNA in water samples from the Florida Everglades for evidence of invasive constrictor snakes, which are difficult to observe.",
            "B) An analysis of eDNA can detect the presence of invasive species that are difficult to observe, such as constrictor snakes.",
            "C) Researchers found Burmese python eDNA, or environmental DNA, in water samples; eDNA is the DNA in released cellular materials, such as shed skin cells.",
            "D) Sara Oyler-McCance’s researchers analyzed environmental DNA (eDNA)—that is, DNA from cellular materials released by organisms—in water samples from the Florida Everglades.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A presents the study assuming familiarity with eDNA — using the term without defining it. Choice B doesn't present the specific study. Choice C defines eDNA, which is unnecessary for an already-familiar audience. Choice D also defines eDNA and doesn't present the study's findings.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "b513efa9",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Species belonging to the Orchidaceae (orchid) family can be found in both tropical and temperate environments.\n"
            "• Orchidaceae species diversity has not been well studied in temperate forests, such as those in Oaxaca, Mexico.\n"
            "• Arelee Estefanía Muñoz-Hernández led a study to determine how many different Orchidaceae species are present in the forests of Oaxaca.\n"
            "• Muñoz-Hernández and her team collected orchids each month for a year at a site in Oaxaca.\n"
            "• Seventy-four Orchidaceae species were present at the site.\n\n"
            "The student wants to present the study and its findings. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) A study led by Arelee Estefanía Muñoz-Hernández identified a total of 74 Orchidaceae species in the temperate forests of Oaxaca, Mexico.",
            "B) There are orchids in many environments, but there are 74 Orchidaceae species in Oaxaca, Mexico.",
            "C) Oaxaca, Mexico, is home to temperate forests containing 74 Orchidaceae species.",
            "D) Arelee Estefanía Muñoz-Hernández and her team wanted to know how many different Orchidaceae species are present in the forests of Oaxaca, Mexico, so they conducted a study to collect orchids.",
        ],
        "correct_answer": "A",
        "explanation": "Choice A presents both the study (led by Muñoz-Hernández) and its finding (74 Orchidaceae species identified). Choice B doesn't mention a study at all. Choice C doesn't mention a study at all. Choice D describes the research goal and method but omits the findings.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "368d0222",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• The Pueblo of Zuni is located about 150 miles west of Albuquerque, New Mexico.\n"
            "• It is the traditional home of the A:shiwi (Zuni) people.\n"
            "• The A:shiwi A:wan Museum and Heritage Center was established by tribal members in 1992.\n"
            "• Its mission is stated on its website: “As a tribal museum and heritage center for the Zuni people and by the Zuni people we work to provide learning experiences that emphasize A:shiwi ways of knowing, as well as exploring modern concepts of knowledge and the transfer of knowledge.”\n\n"
            "The student wants to emphasize how long the museum has existed. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) The Pueblo of Zuni is home to the A:shiwi A:wan Museum and Heritage Center, which was founded by tribal members.",
            "B) The A:shiwi A:wan Museum and Heritage Center has served the Pueblo of Zuni since 1992.",
            "C) According to its website, the A:shiwi A:wan Museum and Heritage Center (founded in the 1990s) works to “emphasize A:shiwi ways of knowing.”",
            "D) Knowledge has been one of the central themes of the A:shiwi A:wan Museum and Heritage Center from its founding.",
        ],
        "correct_answer": "B",
        "explanation": "Choice B effectively emphasizes how long the museum has existed by stating it has served since 1992. Choice A says it was founded by tribal members but doesn't say when. Choice C says 'founded in the 1990s' without a specific year, and focuses on the mission. Choice D doesn't say when the museum was founded.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "a3df6d00",
        "question_text": (
            "Because an achiral molecule is symmetrical, flipping it yields a structurally identical molecule. "
            "A flipped chiral molecule, ______ can be compared to a glove that has been turned inside out: "
            "it produces a structurally inverted molecule rather than an identical one.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) in other words,",
            "B) by contrast,",
            "C) for example,",
            "D) similarly,",
        ],
        "correct_answer": "B",
        "explanation": '"By contrast" fits because flipping a chiral molecule (produces an inverted molecule) is the opposite of flipping an achiral molecule (produces an identical molecule). Choice A (in other words) implies restatement of the same idea. Choice C (for example) implies the chiral molecule exemplifies the achiral claim. Choice D (similarly) implies they behave the same way, which is incorrect.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "cf842c88",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Wool is a natural—and economically important—fiber that is obtained from animals like sheep.\n"
            "• Australia is a leading producer of wool.\n"
            "• The thickness of wool fibers varies across sheep breeds.\n"
            "• Merino sheep produce fine wool that is used for apparel.\n"
            "• Rambouillet sheep produce fine wool that is used for apparel.\n"
            "• Romney sheep produce thick wool that is used for rugs and blankets.\n\n"
            "The student wants to emphasize how Romney wool differs from Merino and Rambouillet wool. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Romney wool is just one of the many kinds of wools, each originating from a different breed of sheep.",
            "B) Sheep wool varies from breed to breed, so Romney wool will be different than other kinds of wool.",
            "C) The fine wool produced by Merino and Rambouillet sheep is used for apparel, whereas the thicker wool of Romney sheep is used in rugs and blankets.",
            "D) Wool is an economically important fiber—especially in Australia—that can be used to make apparel or even rugs and blankets.",
        ],
        "correct_answer": "C",
        "explanation": "Choice C emphasizes how Romney wool differs — thickness (thick vs. fine) and use (rugs/blankets vs. apparel). Choice A doesn't mention Merino or Rambouillet. Choice B doesn't mention Merino or Rambouillet. Choice D doesn't mention Romney, Merino, or Rambouillet wool at all.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "274d8844",
        "question_text": (
            "Okot p’Bitek’s poem Song of Lawino (1966) explores postcolonial Ugandan life through the eyes of a woman living in a rural village. "
            "With its vibrant imagery, bitingly satiric tone, and dexterous use of traditional Acholi song and phraseology, the poem inspired "
            "a generation of East African writers. ______ those who adopted its style are often referred to as Okot School poets.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) Nevertheless,",
            "B) Fittingly,",
            "C) By comparison,",
            "D) Instead,",
        ],
        "correct_answer": "B",
        "explanation": '"Fittingly" means "appropriately" — it is appropriate that writers who adopted Okot p\'Bitek\'s style would be known as the Okot School poets. Choice A (nevertheless) is a disagreement transition, but this sentence doesn\'t disagree. Choice C (by comparison) compares two ideas, but this sentence isn\'t making a comparison. Choice D (instead) is a disagreement transition that doesn\'t fit.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "dd8a1d0d",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In 2017, a research team led by Mary Caswell Stoddard determined the average lengths of eggs produced by various bird species.\n"
            "• Gygis alba is a species of bird in the order Charadriiformes.\n"
            "• Gygis alba eggs had an average length of 4.46 cm.\n"
            "• Gavia stellata is a species of bird in the order Gaviiformes.\n"
            "• Gavia stellata eggs had an average length of 7.22 cm.\n\n"
            "Which choice most effectively uses information from the given sentences to emphasize a difference between the eggs of the two species?"
        ),
        "choices": [
            "A) A 2017 study compared the lengths of eggs produced by an array of different bird species, such as Gygis alba and Gavia stellata.",
            "B) A 2017 study found that Gygis alba eggs had an average length of 4.46 cm, whereas Gavia stellata eggs were longer, with an average length of 7.22 cm.",
            "C) The bird species Gygis alba, which belongs to the order Charadriiformes, and Gavia stellata, of the order Gaviiformes, were included in a 2017 study that compared the average lengths of their eggs.",
            "D) Mary Caswell Stoddard led a research study that determined the average lengths of eggs, including those of Gygis alba birds (4.46 cm) and Gavia stellata birds (7.22 cm).",
        ],
        "correct_answer": "B",
        "explanation": "Choice B emphasizes the difference by directly contrasting the shorter Gygis alba average (4.46 cm) with the longer Gavia stellata average (7.22 cm). Choice A mentions both species without emphasizing a difference. Choice C provides information about the species but doesn't emphasize a difference between their eggs. Choice D lists both lengths without explicitly emphasizing the difference.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "de17a78b",
        "question_text": (
            "Voting members of the 2002 Latin Grammys were impressed by Banda Cuisillos’s album Puras Rancheras Con Cuisillos and its "
            "contribution to the banda genre, a form of regional Mexican music featuring large ensembles of wind instruments and drums that "
            "first developed in southern and central Mexico in the mid-nineteenth century. ______ they awarded the group the Best Banda Album award.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) In contrast,",
            "B) Meanwhile,",
            "C) Nevertheless,",
            "D) Accordingly,",
        ],
        "correct_answer": "D",
        "explanation": '"Accordingly" signals that awarding the Best Banda Album is in accordance with, or results from, the voters being impressed. Choice A (in contrast) implies the award contrasts with the impression. Choice B (meanwhile) implies separation rather than a result. Choice C (nevertheless) implies the award was given despite the impression, which is the opposite of what happened.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "a0903efe",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• In the midst of the US Civil War, Susie Taylor escaped slavery and fled to Union-army-occupied St. Simons Island off the Georgia coast.\n"
            "• She began working for an all-Black army regiment as a nurse and teacher.\n"
            "• In 1902, she published a book about the time she spent with the regiment.\n"
            "• Her book was the only Civil War memoir to be published by a Black woman.\n"
            "• It is still available to readers in print and online.\n\n"
            "The student wants to emphasize the uniqueness of Taylor’s accomplishment. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Taylor fled to St. Simons Island, which was then occupied by the Union army, for whom she began working.",
            "B) After escaping slavery, Taylor began working for an all-Black army regiment as a nurse and teacher.",
            "C) The book Taylor wrote about the time she spent with the regiment is still available to readers in print and online.",
            "D) Taylor was the only Black woman to publish a Civil War memoir.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D emphasizes the uniqueness of Taylor's accomplishment by stating she was the only Black woman to publish a Civil War memoir. Choice A describes some accomplishments without emphasizing uniqueness. Choice B describes accomplishments without emphasizing uniqueness. Choice C provides information about the book's availability without emphasizing what made it unique.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "2138137b",
        "question_text": (
            "The chemical trimethylamine N-oxide not only gives fish their fishy smell but also protects them from crushing hydrostatic "
            "pressure in deep waters. Trimethylamine N-oxide strengthens the bonds between water molecules in a fish’s body. "
            "______ these water molecules maintain their linked structure at extreme depths, thus preventing pressure-related damage.\n\n"
            "Which choice completes the text with the most logical transition?"
        ),
        "choices": [
            "A) Nevertheless,",
            "B) As a result,",
            "C) However,",
            "D) For instance,",
        ],
        "correct_answer": "B",
        "explanation": '"As a result" signals that water molecules maintaining their structure is caused by trimethylamine N-oxide strengthening the bonds. Choices A and C (nevertheless, however) are disagreement transitions, but this sentence describes an effect. Choice D (for instance) implies an example of the previous claim, but this sentence describes a consequence.',
        "domain": "Expression of Ideas",
        "skill": "Transitions",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "2f3202d5",
        "question_text": (
            "While researching a topic, a student has taken the following notes:\n"
            "• Platinum is a rare and expensive metal.\n"
            "• It is used as a catalyst for chemical reactions.\n"
            "• Platinum catalysts typically require a large amount of platinum to be effective.\n"
            "• Researcher Jianbo Tang and his colleagues created a platinum catalyst that combines platinum with liquid gallium.\n"
            "• Their catalyst was highly effective and required only trace amounts of platinum (0.0001% of the atoms in the mixture).\n\n"
            "The student wants to explain an advantage of the new platinum catalyst developed by Jianbo Tang and his colleagues. Which choice most effectively uses relevant information from the notes to accomplish this goal?"
        ),
        "choices": [
            "A) Researcher Jianbo Tang and his colleagues created a platinum catalyst that combines platinum, a rare and expensive metal, with liquid gallium.",
            "B) Like other platinum catalysts, the new platinum catalyst requires a particular amount of the metal to be effective.",
            "C) Platinum is a rare and expensive metal that is used as a catalyst for chemical reactions; however, platinum catalysts typically require a large amount of platinum to be effective.",
            "D) While still highly effective, the new platinum catalyst requires far less of the rare and expensive metal than do other platinum catalysts.",
        ],
        "correct_answer": "D",
        "explanation": "Choice D explains the advantage — the new catalyst requires far less platinum than other platinum catalysts while remaining highly effective. Choice A describes what Tang created without explaining an advantage. Choice B emphasizes a similarity, not an advantage. Choice C connects platinum to catalyst functioning but doesn't explain an advantage of the new catalyst.",
        "domain": "Expression of Ideas",
        "skill": "Rhetorical Synthesis",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
]


def main():
    print(f"Embedding {len(QUESTIONS)} questions…")
    embed_batch(QUESTIONS)

    jsonl_path = "data/structured/expression_of_ideas_medium.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for q in QUESTIONS:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(f"Saved {jsonl_path}")

    collection = get_collection()
    ids, embeddings, documents, metadatas = [], [], [], []
    for q in QUESTIONS:
        ids.append(q["id"])
        embeddings.append(q["embedding"])
        documents.append(q["question_text"])
        metadatas.append({
            "domain": q["domain"],
            "skill": q["skill"],
            "difficulty": q["difficulty"],
            "source": q["source"],
            "correct_answer": q["correct_answer"],
            "choices": json.dumps(q["choices"]),
            "explanation": q["explanation"],
            "calculator_allowed": q.get("calculator_allowed") or "",
            "image_path": q.get("image_path") or "",
        })

    collection.upsert(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)
    print(f"Collection now has {collection.count()} total records.")


if __name__ == "__main__":
    main()
