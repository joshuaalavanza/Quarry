"""One-off ingestion script for medium Standard English Conventions questions."""
from __future__ import annotations
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ingestion.embed import embed_batch
from ingestion.load import get_collection

QUESTIONS = [
    {
        "id": "fd5268ad",
        "question_text": (
            "Oglala Lakota poet Layli Long Soldier's star quilt poems offer an unusually open-ended reading experience. "
            "With ______ eight panels of text stitched together in the shape of a traditional eight-pointed Lakota star quilt, "
            "the poems present viewers with a seemingly infinite number of ways to read them.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) their", "B) it's", "C) they're", "D) its"],
        "correct_answer": "A",
        "explanation": "\"Their\" is the plural possessive determiner that agrees in number with the plural noun \"the poems,\" correctly indicating that the poems have eight panels. \"It's\" and \"they're\" are contractions (it is/it has and they are), not possessive determiners. The singular possessive \"its\" doesn't agree with the plural \"the poems.\"",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "296f8a05",
        "question_text": (
            "Based on genetic evidence, archaeologists have generally agreed that reindeer domestication began in the eleventh century CE. "
            "However, since uncovering fragments of a 2,000-year-old reindeer training harness in northern Siberia, ______ may have begun much earlier.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) researcher Robert Losey has argued that domestication",
            "B) researcher Robert Losey's argument is that domestication",
            "C) domestication, researcher Robert Losey has argued,",
            "D) the argument researcher Robert Losey has made is that domestication",
        ],
        "correct_answer": "A",
        "explanation": "Choice A places \"researcher Robert Losey\" immediately after the modifying phrase \"since…Siberia,\" correctly identifying him as the person who uncovered the harness fragments. Choices B, C, and D all result in dangling modifiers: they place \"argument,\" \"domestication,\" or \"the argument\" after the modifying phrase, illogically suggesting that one of these nouns uncovered the harness fragments.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "c4ff1125",
        "question_text": (
            "Humans were long thought to have begun occupying the Peruvian settlement of Machu Picchu between 1440 and 1450 CE. "
            "However, a team led by anthropologist Dr. Richard Burger used accelerator mass spectrometry to uncover evidence that it was occupied "
            "______ 1420 CE, according to Burger, humans were likely inhabiting the area.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) earlier. In", "B) earlier, in", "C) earlier, which in", "D) earlier in"],
        "correct_answer": "A",
        "explanation": "A period correctly separates the two independent clauses (\"However…earlier\" and \"In…area\"), with \"In 1420 CE\" beginning the new sentence as a modifier of \"humans.\" Choice B is a comma splice. Choice C creates a comma splice and an illogical subordination. Choice D is a run-on — two independent clauses fused without punctuation.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "95649ca9",
        "question_text": (
            "In 1727, dramatist Lewis Theobald presented a new play, Double Falsehood, at a London theater. "
            "Theobald claimed that his drama was based on a little-known play by William Shakespeare, Cardenio. "
            "Many, including poet Alexander Pope, were ______ historians have determined that Shakespeare's company did perform a play called Cardenio in 1613.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) skeptical but", "B) skeptical, but", "C) skeptical,", "D) skeptical"],
        "correct_answer": "B",
        "explanation": "The sentence has two independent clauses (\"Many…were skeptical\" and \"historians have determined…\") that must be joined by a comma and the coordinating conjunction \"but.\" Choice A is a run-on — two independent clauses can't be joined by just a conjunction without a comma. Choice C is a comma splice. Choice D is also a run-on.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "9360277c",
        "question_text": (
            "In 2008, two years after the death of science fiction writer Octavia Butler, the Huntington Library in ______ received a collection of "
            "more than 8,000 items, including Butler's private notes, research materials, manuscripts, photos, and drawings. "
            "Today, the Octavia E. Butler Collection is one of the most researched archives at the library.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) California,", "B) California:", "C) California—", "D) California"],
        "correct_answer": "D",
        "explanation": "No punctuation should separate a subject from its verb. Here, \"the Huntington Library in California\" is the subject and \"received\" is its verb — inserting a comma, colon, or dash between them all create punctuation errors.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "cf86d6fd",
        "question_text": (
            "By the time Hawaiian king Kamehameha III ______ the throne, the number of longhorn cattle, first introduced to the islands in 1793, "
            "had drastically increased, and so too had the need for paniolo (Hawaiian cowboys) to manage the wild herds that then roamed throughout the volcanic terrain.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) ascended", "B) will ascend", "C) ascends", "D) is ascending"],
        "correct_answer": "A",
        "explanation": "The simple past \"ascended\" is correct — Kamehameha III became king in the past, and the tense of other verbs in the sentence (\"had drastically increased,\" \"had\") confirms a past-tense context. \"Will ascend\" is future, \"ascends\" is simple present, and \"is ascending\" is present continuous — all incorrect for a historical event.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "094e6e94",
        "question_text": (
            "The human brain is primed to recognize faces—so much so that, due to a perceptual tendency called pareidolia, "
            "______ will even find faces in clouds, wooden doors, pieces of fruit, and other faceless inanimate objects. "
            "Researcher Susan Magsamen has focused her work on better understanding this everyday phenomenon.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) she", "B) they", "C) it", "D) those"],
        "correct_answer": "C",
        "explanation": "The antecedent is the singular noun phrase \"the human brain,\" which requires the singular pronoun \"it\" (used for objects). \"She\" is for people/animals, not objects. \"They\" and \"those\" are plural pronouns that don't agree with the singular antecedent.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "b79670a7",
        "question_text": (
            "Santa Clara Pueblo artist Roxanne Swentzell's sculpture Mud Woman Rolls On consists of five human figures made of clay and "
            "plant fiber and arranged in descending size; each figure holds the smaller one in front of it. "
            "The arrangement of the figures, according to ______ represents her idea that \"we all come from the Earth, generation after generation.\"\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) Swentzell", "B) Swentzell,", "C) Swentzell:", "D) Swentzell—"],
        "correct_answer": "B",
        "explanation": "The aside \"according to Swentzell\" interrupts the sentence flow and needs a pair of matching punctuation marks. A comma already appears before \"according,\" so a comma after \"Swentzell\" is required to match. A colon would be incorrect after a non-independent clause, and a dash would require a matching dash rather than the comma already present.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "d173443c",
        "question_text": (
            "Luci Tapahonso is the inaugural poet laureate of the Navajo Nation. "
            "Her book Sáanii Dahataal/The Women Are Singing—a combination of fiction and memoir, poetry and ______ serves as a testament to her versatility as a writer.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) prose;", "B) prose", "C) prose,", "D) prose—"],
        "correct_answer": "D",
        "explanation": "\"A combination of fiction and memoir, poetry and prose\" is a nonessential supplement that must be closed with a dash to match the opening dash that appears before it. A semicolon, no punctuation, or a comma all fail to correctly close the dash-opened supplement.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "fd02bdb9",
        "question_text": (
            "According to Naomi Nakayama of the University of Edinburgh, the reason seeds from a dying dandelion appear to float in the air "
            "while ______ is that their porous plumes enhance drag, allowing the seeds to stay airborne long enough for the wind to disperse them throughout the surrounding area.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) falling,", "B) falling:", "C) falling;", "D) falling"],
        "correct_answer": "D",
        "explanation": "\"Falling\" occurs in the middle of a clause and is not part of a supplement, so no punctuation is needed after it. Simplified: \"The reason seeds appear to float while falling is that their plumes enhance drag.\" Any punctuation here would incorrectly separate parts of a continuous clause.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "8e27d086",
        "question_text": (
            "Beatrix Potter is perhaps best known for writing and illustrating children's books such as The Tale of Peter Rabbit (1902), "
            "but she also dedicated herself to mycology, the study of ______ more than 350 paintings of the fungal species she observed in nature "
            "and submitting her research on spore germination to the Linnean Society of London.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) fungi; producing", "B) fungi. Producing", "C) fungi producing", "D) fungi, producing"],
        "correct_answer": "D",
        "explanation": "A comma correctly separates the supplementary noun phrase \"the study of fungi\" (defining mycology) from the supplementary participial phrase \"producing…London\" (adding detail). A semicolon can't join two supplementary phrases this way. A period creates a fragment. No punctuation makes it seem that the study of fungi is itself producing the paintings.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "09333379",
        "question_text": (
            "Nine months before Rosa Parks made history by refusing to comply with the segregated seating policy on a Montgomery, Alabama, bus, "
            "a fifteen-year-old Montgomery girl named Claudette Colvin was arrested for the same ______ to some historians, "
            "Colvin's arrest led to Parks's action and eventually to the desegregation of Montgomery's bus system.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) offense. According", "B) offense, according", "C) offense according", "D) offense and according"],
        "correct_answer": "A",
        "explanation": "\"Nine months…offense\" and \"according to…system\" are both independent clauses; a period is the only provided option that correctly separates them. Choice B is a comma splice. Choice C is a run-on. Choice D uses a coordinating conjunction without the required comma before it.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "8bd8f58c",
        "question_text": (
            "The violins handmade in the seventeenth century by Italian craftsman Antonio Stradivari have been celebrated as some of the finest in the world. "
            "In close collaboration with musicians, Stradivari introduced changes to the shape of a traditional violin, "
            "flattening some of the instrument's curves and making ______ lighter overall.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) those", "B) one", "C) them", "D) it"],
        "correct_answer": "D",
        "explanation": "The singular pronoun \"it\" agrees with the singular antecedent \"violin,\" making clear that Stradivari made the violin (not its curves) lighter overall. \"Those\" and \"them\" are plural and don't agree with the singular \"violin.\" \"One\" is ambiguous and leaves unclear what was made lighter.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "992e6994",
        "question_text": (
            "Far from being modern inventions, ______ more than 5,000 years ago.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) Sumerians in ancient Mesopotamia used drinking straws",
            "B) drinking straws were used by Sumerians in ancient Mesopotamia",
            "C) the use of drinking straws by Sumerians in ancient Mesopotamia happened",
            "D) ancient Mesopotamia was home to Sumerians who used drinking straws",
        ],
        "correct_answer": "B",
        "explanation": "The modifier \"far from being modern inventions\" must be placed next to what it describes — \"drinking straws,\" the only inventions in the sentence. Choice A puts \"Sumerians\" next to the modifier (people aren't inventions). Choice C puts \"the use\" next to it (the use isn't an invention). Choice D puts \"ancient Mesopotamia\" next to it (a place isn't an invention).",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "4ca5ab4d",
        "question_text": (
            "The Mesoamerican city of Teotihuacan featured a uniquely egalitarian urban housing infrastructure. "
            "Built between the first and seventh centuries CE, Teotihuacan housed its residents (as many as 200,000, by some ______ in a complex of comfortable apartments of comparable size.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) estimates)", "B) estimates),", "C) estimates—", "D) estimates"],
        "correct_answer": "A",
        "explanation": "The parenthetical \"as many as 200,000, by some estimates\" must be closed with a parenthesis to match the opening parenthesis. Choice B incorrectly adds a comma after the closing parenthesis, which isn't needed before the prepositional phrase. Choice C uses a dash, which can't pair with an opening parenthesis. Choice D leaves the parenthetical unclosed.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "4efacd65",
        "question_text": (
            "Nuhād al-Ḥaddād, known as Fairuz, was one of the most beloved Lebanese singers of the twentieth century. "
            "Her broad singing repertoire—which included traditional forms, such as the Arabic qasida and maqam, alongside modern pop and jazz styles—lent "
            "Fairuz a timeless, cross-generational appeal, ______ her the moniker \"the soul of Lebanon.\"\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) earned", "B) had earned", "C) earning", "D) earn"],
        "correct_answer": "C",
        "explanation": "\"Earning\" is a participial (-ing) verb form used without a helper verb to introduce an additional modifying phrase — it correctly describes the result of Fairuz's cross-generational appeal. Finite verb forms (\"earned,\" \"had earned,\" \"earn\") create an error because the underlined portion has no subject of its own.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "21922a16",
        "question_text": (
            "The Proto-Nilotic language, common ancestor of fifty-five African languages with similar linguistic properties, ______ like all protolanguages, "
            "hypothetical: there's no direct evidence these ancestral languages actually existed.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) is,", "B) are,", "C) have been,", "D) were,"],
        "correct_answer": "A",
        "explanation": "The singular verb \"is\" agrees with the singular subject \"the Proto-Nilotic language.\" The intervening phrase \"common ancestor of fifty-five African languages\" can be removed to verify: \"The Proto-Nilotic language is…hypothetical.\" \"Are,\" \"have been,\" and \"were\" are all plural.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "130a364f",
        "question_text": (
            "The first computerized spreadsheet, Dan Bricklin's VisiCalc, improved financial recordkeeping not only by providing users with an easy means "
            "of adjusting data in spreadsheets but also by automatically updating all calculations that were dependent on these "
            "______ to VisiCalc's release, changing a paper spreadsheet often required redoing the entire sheet by hand, a process that could take days.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) adjustments prior",
            "B) adjustments, prior",
            "C) adjustments. Prior",
            "D) adjustments and prior",
        ],
        "correct_answer": "C",
        "explanation": "A period correctly separates the first sentence (\"The…adjustments\") from the second (\"Prior…days\"), with the adverbial phrase \"Prior to VisiCalc's release\" belonging to the second sentence. Choice A is a run-on. Choice B is a comma splice. Choice D uses a conjunction without the required comma.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "35c6af60",
        "question_text": (
            "Swedish scientists Eva Engvall and Peter Perlmann developed a method for measuring the concentration of different proteins in a biological sample. "
            "Their ______ ELISA (enzyme-linked immunosorbent assay), is used to detect and measure proteins that indicate the presence of certain diseases.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) method (called", "B) method—called", "C) method, called", "D) method called"],
        "correct_answer": "C",
        "explanation": "A comma after \"method\" pairs with the comma after the closing parenthesis to correctly set off the supplementary element \"called ELISA (enzyme-linked immunosorbent assay).\" An opening parenthesis can't pair with a comma, a dash can't pair with a comma, and no punctuation fails to mark the supplementary element.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "b249902a",
        "question_text": (
            "Detroit natives Timothy Paule and Nicole Lindsey have combined their two passions, Detroit and beekeeping, to improve the health of their city's flowers and other vegetation. "
            "In 2017, the couple converted a vacant lot in the city into an ______ in the years that followed they acquired nine additional lots and established more than 35 hives.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) apiary,", "B) apiary, and", "C) apiary and", "D) apiary"],
        "correct_answer": "B",
        "explanation": "The sentence contains two independent clauses that must be joined with a comma plus a coordinating conjunction. Choice B provides the comma and \"and\" needed to properly link them. Choice A is a comma splice. Choice C is missing the required comma before the conjunction. Choice D is a run-on with no punctuation between the two clauses.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "9b49630d",
        "question_text": (
            "Materials scientist Marie-Agathe Charpagne and her colleagues believed they could improve on the multicomponent alloy NiCoCr, "
            "an equal-proportions mixture of nickel (Ni), cobalt (Co), and chromium (Cr), by replacing chromium with ruthenium ______ the alloy that resulted, NiCoRu, turned out to be an unsuitable replacement for NiCoCr.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) (Ru)", "B) (Ru) but", "C) (Ru),", "D) (Ru), but"],
        "correct_answer": "D",
        "explanation": "Two main clauses must be joined with a comma and the coordinating conjunction \"but.\" Choice D correctly provides both. Choice A is a run-on. Choice B omits the required comma before a coordinating conjunction joining longer main clauses. Choice C is a comma splice — a comma alone can't join two main clauses.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "b305e581",
        "question_text": (
            "How do scientists determine what foods were eaten by extinct hominins such as Neanderthals? In the past, researchers were limited to studying the marks found on the fossilized teeth of skeletons, "
            "but in 2017 a team led by Laura Weyrich of the Australian Centre for Ancient DNA tried something ______ the DNA found in Neanderthals' fossilized dental plaque.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) new: sequencing", "B) new; sequencing", "C) new, sequencing:", "D) new. Sequencing"],
        "correct_answer": "A",
        "explanation": "\"A team…tried something new\" is an independent clause leading into an explanation. A colon correctly follows an independent clause to introduce further explanation (\"sequencing the DNA…\"). Choice B is incorrect — a semicolon requires two independent clauses, and \"sequencing…dental plaque\" can't stand alone. Choice C puts the colon after a non-independent clause. Choice D creates a sentence fragment (\"Sequencing…dental plaque\" has no subject).",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "a3f9a509",
        "question_text": (
            "Inventor John Friedman created a prototype of the first flexible straw by inserting a screw into a paper straw and, "
            "using dental floss, binding the straw tightly around the ______ When the floss and screw were removed, "
            "the resulting corrugations in the paper allowed the straw to bend easily over the edge of a glass.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) screw's thread's.", "B) screws' threads.", "C) screw's threads.", "D) screws threads'."],
        "correct_answer": "C",
        "explanation": "\"Screw's\" is the singular possessive (there is one screw), and \"threads\" is the simple plural (the screw has multiple threads — nothing belongs to them). Choice A incorrectly makes \"threads\" possessive. Choice B incorrectly uses the plural possessive \"screws'.\" Choice D has \"screws\" (plural, no possession) and \"threads'\" (plural possessive), both wrong.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "6203926e",
        "question_text": (
            "In ancient Greece, an Epicurean was a follower of Epicurus, a philosopher whose beliefs revolved around the pursuit of pleasure. "
            "Epicurus defined pleasure as \"the absence of pain in the body and of trouble in the ______ that all life's virtues derived from this absence.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ['A) soul," positing', 'B) soul": positing', 'C) soul"; positing', 'D) soul." Positing'],
        "correct_answer": "A",
        "explanation": "A comma correctly marks the boundary between the main clause (\"Epicurus…'soul'\") and the participial phrase (\"positing…absence\") that provides additional information. A colon or semicolon can't join a main clause and a participial phrase. A period creates a sentence fragment beginning with \"Positing.\"",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "736ac5f3",
        "question_text": (
            "Anthropologist Lívia Barbosa, of the Universidade Federal Fluminense in Brazil, ______ food and sociability in contemporary Brazil—specifically, "
            "how foods such as cabidela (a rice and rabbit dish) and churrasco (a barbeque dish) function as central mechanisms in building social relationships, values, and identities.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) studies", "B) are studying", "C) have studied", "D) study"],
        "correct_answer": "A",
        "explanation": "The singular verb \"studies\" agrees with the singular subject \"anthropologist Lívia Barbosa.\" The intervening prepositional phrase \"of the Universidade Federal Fluminense in Brazil\" doesn't change the subject. \"Are studying,\" \"have studied,\" and \"study\" are all plural.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "d0884ae5",
        "question_text": (
            "Official measurements of the Mississippi River's length vary: according to the US Geologic Survey, the river is 2,300 miles long, "
            "whereas the Environmental Protection Agency records its length as 2,320 miles. This disparity can be explained in part by the fact "
            "that rivers such as the Mississippi expand and contract as ______ sediment.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) they accumulate", "B) one accumulates", "C) it accumulates", "D) we accumulate"],
        "correct_answer": "A",
        "explanation": "\"They\" is the correct third-person plural pronoun agreeing with the plural noun \"rivers,\" which is the subject of \"expand and contract.\" \"One\" and \"it\" are singular and don't agree with the plural \"rivers.\" \"We\" can't stand in for a noun referring to things (rivers are not people).",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "87eb538d",
        "question_text": (
            "Because a cycle of lunar phases ______ 29.5 days to complete, it's possible to observe two full moons in a single month, one at the beginning and one at the end.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) are taking", "B) have taken", "C) take", "D) takes"],
        "correct_answer": "D",
        "explanation": "The singular verb \"takes\" agrees with the singular subject \"a cycle of lunar phases.\" \"Phases\" is the object of the preposition \"of,\" not the subject. \"Are taking,\" \"have taken,\" and \"take\" are all plural.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "2ee3c97f",
        "question_text": (
            "Every last second of space shuttle mission STS-79, which lasted ten days and three hours, ______ carefully monitored by a team of experts.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) have been", "B) are", "C) was", "D) were"],
        "correct_answer": "C",
        "explanation": "The singular verb \"was\" agrees with the singular subject \"every last second.\" The relative clause \"which lasted ten days and three hours\" is a modifier, not the subject. \"Have been,\" \"are,\" and \"were\" are all plural.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "f6572385",
        "question_text": (
            "Professional American football player Fred Cox invented one of the world's most popular toys. "
            "In the 1970s, he came up with the idea for the Nerf football, which ______ of the harder and heavier regulation football.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) were a smaller, foam version",
            "B) are smaller, foam versions",
            "C) were smaller, foam versions",
            "D) is a smaller, foam version",
        ],
        "correct_answer": "D",
        "explanation": "The relative pronoun \"which\" refers to the singular noun \"the Nerf football,\" so both the verb (\"is\") and the noun (\"version\") must be singular. Choices A and C use the plural past \"were.\" Choice B uses the plural present \"are\" and plural \"versions.\"",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "1ea3651d",
        "question_text": (
            "Classical composer Florence Price's 1927 move to Chicago marked a turning point in her career. "
            "It was there that Price premiered her First Symphony—a piece that was praised for blending traditional Romantic motifs with aspects of Black folk music—and "
            "______ supportive relationships with other Black artists.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) developing", "B) developed", "C) to develop", "D) having developed"],
        "correct_answer": "B",
        "explanation": "\"Developed\" matches the parallel past-tense verb \"premiered\" — both share \"Price\" as their subject in the same clause (\"Price premiered…and developed\"). \"Developing,\" \"to develop,\" and \"having developed\" are all non-parallel verb forms that don't match \"premiered.\"",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "d7b89c91",
        "question_text": (
            "Gathering accurate data on water flow in the United States is challenging because of the country's millions of miles of ______ the volume and speed of water at any given location can vary drastically over time.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) waterways and the fact that,",
            "B) waterways, and the fact that,",
            "C) waterways, and, the fact that",
            "D) waterways and the fact that",
        ],
        "correct_answer": "D",
        "explanation": "When two noun phrases (\"the country's millions of miles of waterways\" and \"the fact\") are coordinated and followed by an integrated relative clause (\"that the volume…time\"), no punctuation is needed between them. All other choices introduce unnecessary commas.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "72ae84d8",
        "question_text": (
            "Slam poet Elizabeth Acevedo's debut novel The Poet X, winner of the 2018 National Book Award for Young People's Literature, is composed of "
            "______ protagonist, fifteen-year-old Xiomara Batista.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) poems putatively written by the novel's",
            "B) poem's putatively written by the novel's",
            "C) poem's putatively written by the novels'",
            "D) poems putatively written by the novels'",
        ],
        "correct_answer": "A",
        "explanation": "\"Poems\" should be a simple plural (there are multiple poems, nothing belongs to them). \"Novel's\" should be the singular possessive (the protagonist belongs to the one novel). Choice B makes \"poem's\" possessive incorrectly. Choice C has both errors. Choice D correctly pluralizes \"poems\" but incorrectly uses the plural possessive \"novels'\" for one novel.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "0b05d2d6",
        "question_text": (
            "The 2022 Nobel Prize in Chemistry was awarded to three pioneers in the field of click chemistry: "
            "two-time Nobel laureate Barry Sharpless, who coined the term \"click chemistry\" in 1998; "
            "Carolyn Bertozzi, founder of the Bertozzi Group at ______ and Morten Meldal, a professor at the University of Copenhagen in Denmark.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) Stanford", "B) Stanford,", "C) Stanford:", "D) Stanford;"],
        "correct_answer": "D",
        "explanation": "This is a complex list where items contain internal commas (e.g., \"Barry Sharpless, who coined…1998\"), so semicolons must separate the list items. A semicolon after \"Stanford\" correctly separates Bertozzi's entry from Meldal's. No punctuation, a comma, or a colon all fail to properly separate items in a complex semicolon-delimited list.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "e6201ac0",
        "question_text": (
            "Archaeologists have estimated that the pre-Columbian Native American city of Cahokia, located across the Mississippi River from modern-day St. Louis, Missouri, "
            "had as many as 20,000 inhabitants in the year 1150 ______ it one of the largest cities in North America at the time.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) CE making", "B) CE. Making", "C) CE, making", "D) CE; making"],
        "correct_answer": "C",
        "explanation": "\"Making…at the time\" is a nonessential participial phrase providing additional information and must be separated from the main clause with a comma. Choice A is a run-on. Choice B creates a sentence fragment (\"Making…at the time\" has no subject). Choice D is incorrect — a semicolon requires two independent clauses, and this phrase isn't one.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "e9a4666c",
        "question_text": (
            "In January 1776, Thomas Paine published Common Sense, an appeal for freedom from the British monarchy that famously helped ignite the desire for independence among the American colonists. "
            "After the colonies achieved their independence, Paine moved to Paris, where the provocative ______ would contribute to another revolution—the French Revolution.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) authors political writings",
            "B) author's political writings",
            "C) author's political writing's",
            "D) authors' political writings'",
        ],
        "correct_answer": "B",
        "explanation": "\"Author's\" is the singular possessive (the writings belong to one author, Thomas Paine), and \"writings\" is the simple plural (multiple works are discussed, nothing belongs to them). \"Authors\" (plural, no possession) is wrong. \"Writing's\" makes the singular possessive, but multiple works are implied. \"Authors'\" and \"writings'\" are both plural possessives, both incorrect.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "e8a33878",
        "question_text": (
            "Josephine Paddock and Florence Esté were among the 300 artists who exhibited at the 1913 Armory Show, a groundbreaking New York City art exhibition that introduced modernism to American audiences. "
            "Though shocking at the time, an abstract cubist painting exhibited by Marcel Duchamp—one of several works that received scorn from critics—______ the Western art canon more than a century later.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) has entered", "B) have entered", "C) were entering", "D) enter"],
        "correct_answer": "A",
        "explanation": "The singular verb \"has entered\" agrees with the singular subject \"an abstract cubist painting.\" The intervening phrase \"one of several works that received scorn from critics\" is a modifier, not part of the subject. \"Have entered,\" \"were entering,\" and \"enter\" are all plural.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "8cfad1fb",
        "question_text": (
            "The Lion Light system, developed by Kenyan inventor Richard Turere, consists of LED lights installed around the perimeter of livestock pastures. "
            "Powered with ______ the blinking LEDs keep lions away at night, thus protecting the livestock without risking harm to the endangered lions.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            "A) energy collected, by solar panels, during the day",
            "B) energy collected by solar panels during the day",
            "C) energy collected by solar panels during the day,",
            "D) energy, collected by solar panels during the day,",
        ],
        "correct_answer": "C",
        "explanation": "A comma after the supplementary phrase \"Powered with energy collected by solar panels during the day\" correctly marks the boundary before the main clause \"the blinking LEDs keep lions away at night.\" Choice A incorrectly isolates \"by solar panels\" as if it's removable. Choice B omits the required boundary comma. Choice D places commas around \"collected by solar panels during the day\" as if that phrase is removable, which isn't the case.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "08fe665d",
        "question_text": (
            "A conceptual artist and designer embraced by both the art world and the fashion ______ Mary Ping was chosen to curate the exhibition Front Row: Chinese American Designers for the Museum of Chinese in America.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) world", "B) world:", "C) world;", "D) world,"],
        "correct_answer": "D",
        "explanation": "A comma correctly marks the boundary between the supplementary phrase \"A conceptual artist and designer embraced by both the art world and the fashion world\" (which describes Mary Ping) and the main clause \"Mary Ping was chosen to curate the exhibition.\" No punctuation creates a run-on. A colon incorrectly implies the supplementary phrase explains the main clause. A semicolon can't join a phrase and a main clause.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "aeba7f69",
        "question_text": (
            "After winning the 1860 presidential election, Abraham Lincoln appointed Edward Bates, Salmon P. Chase, and William H. Seward to his cabinet. "
            "Lincoln's decision was surprising, since each of these men had run against him, but historians have praised it, "
            "noting that Lincoln ______ his rivals' diverse talents to strengthen his administration.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": ["A) has leveraged", "B) is leveraging", "C) will leverage", "D) leveraged"],
        "correct_answer": "D",
        "explanation": "The simple past \"leveraged\" is correct — Lincoln made his cabinet appointments in 1860, a completed past action. \"Has leveraged\" (present perfect) implies the action continues today. \"Is leveraging\" is present tense. \"Will leverage\" is future tense. All three are wrong for a historical event that concluded in 1860.",
        "domain": "Standard English Conventions",
        "skill": "Form, Structure, and Sense",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
    {
        "id": "4449bf81",
        "question_text": (
            "In her analysis of Edith Wharton's The House of Mirth (1905), scholar Candace Waid observes that the novel depicts the upper classes of New York society "
            "as \"consumed by the appetite of a soulless ______ an apt assessment given that The House of Mirth is set during the Gilded Age, "
            "a period marked by rapid industrialization, economic greed, and widening wealth disparities.\n\n"
            "Which choice completes the text so that it conforms to the conventions of Standard English?"
        ),
        "choices": [
            'A) materialism"; and',
            'B) materialism" and',
            'C) materialism,"',
            'D) materialism"',
        ],
        "correct_answer": "C",
        "explanation": "A comma correctly marks the boundary between the main clause (\"scholar…materialism\") and the supplementary noun phrase (\"an apt assessment\") that describes Waid's observation. A semicolon and \"and\" can't join a main clause and a supplementary noun phrase. Using \"and\" alone creates a confusing sentence suggesting the novel depicts the upper classes as \"an apt assessment.\" No punctuation fails to mark the boundary.",
        "domain": "Standard English Conventions",
        "skill": "Boundaries",
        "difficulty": "Medium",
        "calculator_allowed": None,
        "source": "EQB",
        "image_path": None,
    },
]


def main():
    print(f"Embedding {len(QUESTIONS)} questions…")
    embed_batch(QUESTIONS)

    jsonl_path = "data/structured/sec_medium.jsonl"
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
