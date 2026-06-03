"""
One-time ingestion of Craft and Structure Medium questions.
Question data extracted directly from the PDF; no Claude API call needed.
Run:  python ingest_craft_structure_medium.py
Then: python -m ingestion.load data/structured/craft_and_structure_medium.jsonl
"""
from __future__ import annotations
import json
from pathlib import Path
from ingestion.embed import embed_batch

QUESTIONS: list[dict] = [
    {
        "id": "101e69de",
        "question_text": (
            "The following text is from F. Scott Fitzgerald's 1925 novel The Great Gatsby.\n\n"
            "[Jay Gatsby] was balancing himself on the dashboard of his car with that resourcefulness of movement "
            "that is so peculiarly American—that comes, I suppose, with the absence of lifting work in youth and, "
            "even more, with the formless grace of our nervous, sporadic games. This quality was continually "
            "breaking through his punctilious manner in the shape of restlessness.\n\n"
            'As used in the text, what does the word "quality" most nearly mean?'
        ),
        "choices": ["A) Standard", "B) Prestige", "C) Characteristic", "D) Accomplishment"],
        "correct_answer": "C",
        "explanation": (
            'Choice C is the best answer. "This quality" refers to Gatsby\'s "resourcefulness of movement," '
            "which is described as a characteristic or trait of his. "
            'Choice A is incorrect. "Standard" is a synonym for a different definition of "quality": the degree '
            "of excellence of something. "
            'Choice B is incorrect. "Prestige" would suggest a high status or an admirable reputation, which '
            "doesn't match that description. "
            'Choice D is incorrect. "Accomplishment" would suggest an achievement, which doesn\'t match that description.'
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "40e3aa38",
        "question_text": (
            "Text 1\nOne challenge faced by researchers studying global urbanization is that countries may define "
            "urban settlements differently. Many countries define urban settlements based on the number of people "
            "living in them. However, countries do not all use the same number; for example, Iceland uses a minimum "
            "population of 200, while the Netherlands uses 20,000. Other countries use a combination of population "
            "and other factors. This variation makes it difficult for researchers to compare aspects of urbanization "
            "in different countries.\n\n"
            "Text 2\nRecently, a group of six international organizations developed global definitions of common "
            "types of settlements. The group developed a new measure called the \"degree of urbanization.\" This "
            "new measure establishes global criteria used to define three types of settlements (cities, towns, and "
            "rural areas) and allows researchers to better understand global urbanization rates.\n\n"
            "Based on the texts, how would the author of Text 2 most likely respond to the problem presented in Text 1?"
        ),
        "choices": [
            "A) By recommending that a specific institution should further investigate the problem",
            "B) By suggesting that researchers focus on topics besides urbanization",
            "C) By supplying additional ways in which urbanization research is difficult",
            "D) By noting that a possible solution to the problem is available",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer because Text 2 presents a possible solution to the problem identified in "
            "Text 1—that is, how disparities in the criteria used by different countries to define urban settlements "
            "make it \"difficult for researchers to compare aspects of urbanization in different countries.\" Text 2 "
            "describes the creation of a shared framework: \"global definitions of common types of settlements\" and "
            "a \"new measure called the 'degree of urbanization.'\" "
            "Choice A is incorrect because no organization is singled out to perform further research. "
            "Choice B is incorrect because both texts are about urbanization research. "
            "Choice C is incorrect because Text 2 discusses a possible solution, not additional difficulties."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "2f887164",
        "question_text": (
            "The following text is from Virginia Woolf's 1919 novel Night and Day. The text describes a gathering "
            "of young artists and intellectuals.\n\n"
            "One person after another rose, and, as with an ill-balanced axe, attempted to hew out his conception "
            "of art a little more clearly, and sat down with the feeling that, for some reason which he could not "
            "grasp, his strokes had gone awry. As they sat down they turned almost invariably to the person sitting "
            "next them, and rectified and continued what they had just said in public.\n\n"
            "Which choice best describes the function of the underlined portions in the text as a whole?"
        ),
        "choices": [
            "A) To demonstrate individuals' puzzlement over the reputation of a certain artwork",
            "B) To highlight the physical effort involved in individuals' construction of large-scale works of art",
            "C) To draw attention to individuals' discontent with the group's conversation about art",
            "D) To emphasize the extent of individuals' struggles to articulate thoughts on art",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer because the underlined portions describe the young artists and intellectuals "
            "as trying to \"hew out\" their views of art, but with an \"ill-balanced axe\" and feeling that \"strokes "
            "had gone awry.\" The metaphorical language emphasizes how much the individuals struggled to articulate "
            "their thoughts; they couldn't grasp why their statements had gone awry and tried to rectify them afterward. "
            "Choice A is incorrect because the underlined portions characterize attempts to present general views of art, "
            "not views about a specific artwork's reputation. "
            "Choice B is incorrect because the descriptions are metaphorical rather than literal. "
            "Choice C is incorrect because the text focuses on each individual's dissatisfaction with their own statements, "
            "not on how they felt about the group's full conversation."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "dac47b83",
        "question_text": (
            "Stephen Hannock's luminous landscape paintings are appealing to viewers but have elicited little "
            "commentary from contemporary critics, a phenomenon that may be due to the very fact that the paintings "
            "seem so ______. Many critics focus their attention on art that is cryptic or overtly challenging.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) innovative", "B) subversive", "C) profound", "D) accessible"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. \"Accessible\" means easy to understand. This sets up the contrast in the "
            "next sentence, which tells us that critics mostly focus on art that is \"cryptic or challenging.\" "
            "Choice A is incorrect. If Hannock's paintings are \"innovative,\" then critics probably would comment on them. "
            "Choice B is incorrect. If Hannock's paintings are \"subversive,\" then critics probably would comment on them. "
            "Choice C is incorrect. If Hannock's paintings are \"profound,\" then critics probably would comment on them."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "943bdd80",
        "question_text": (
            "Austin McCoy has argued that historians have tended to ______ rank-and-file workers in analyses of "
            "changes in organized labor in the United States in the decades following the Second World War, "
            "presenting political, business, and labor leaders as the major actors and ordinary workers as nearly "
            "devoid of agency.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) epitomize", "B) marginalize", "C) extol", "D) substantiate"],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer because \"marginalize\" means treat as unimportant or relatively powerless. "
            "Historians have treated political, business, and labor leaders as the \"major actors,\" thereby minimizing "
            "the contributions of ordinary workers, treating them as \"nearly devoid of agency.\" "
            "Choice A is incorrect. \"Epitomize\" means serve as an ideal example of, which doesn't fit. "
            "Choice C is incorrect. \"Extol\" means praise highly, which contradicts the text. "
            "Choice D is incorrect. \"Substantiate\" means verify with evidence, which doesn't fit the context."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "fd0c38e6",
        "question_text": (
            "Text 1\nStage lighting theorist Adolphe Appia was perhaps the first to argue that light must be "
            "considered alongside all the various elements of a stage to create a single, unified performance. "
            "Researcher Kelly Bremner, however, has noted that Appia lacked technical expertise in the use of "
            "light in the theater. As a result of Appia's inexperience, Bremner argues, Appia's theory of light "
            "called for lighting practices that weren't possible until after the advent of electricity around 1881.\n\n"
            "Text 2\nAdolphe Appia was not an amateur in the practice of lighting. Instead, it is precisely his "
            "exposure to lighting techniques at the time that contributed to his theory on the importance of light. "
            "When working as an apprentice for a lighting specialist in his youth, Appia observed the use of "
            "portable lighting devices that could be operated by hand. This experience developed his understanding "
            "of what was possible in the coordination of elements on the stage.\n\n"
            "Based on the texts, how would the author of Text 2 most likely respond to the claim about Appia's "
            "level of technical expertise made by Bremner in Text 1?"
        ),
        "choices": [
            "A) Many lighting technicians dismissed Appia's ideas about light on the stage.",
            "B) Appia likely gained a level of technical expertise during his time as an apprentice.",
            "C) Theater practitioners who worked with Appia greatly admired his work.",
            "D) Appia was unfamiliar with the use of music and sound in theater.",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. The author of Text 2 directly contradicts Bremner's claim by stating that "
            "Appia was \"not an amateur in the practice of lighting.\" His experience as a lighting specialist's "
            "apprentice allowed Appia to \"[develop] his understanding of what was possible\" with theatrical design. "
            "Choice A is incorrect because neither text describes how other lighting technicians responded to Appia's ideas. "
            "Choice C is incorrect because neither text mentions the opinions of theater practitioners who worked with Appia. "
            "Choice D is incorrect because neither text mentions Appia's familiarity with music and sound."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "5c9c3bca",
        "question_text": (
            "Mineralogical differences are detectable in samples collected from two locations on the near-Earth "
            "asteroid Ryugu, but such differences may not indicate substantial compositional variations in the "
            "asteroid. Cosmochemist Kazuhide Nagashima and colleagues note that at the small scale of the samples, "
            "the distribution of minerals is unlikely to be ______.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) neglected", "B) redundant", "C) ongoing", "D) uniform"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The text says the samples are too \"small scale\" to reflect the "
            "composition of the asteroid as a whole, suggesting the mineral distribution in small samples is "
            "unlikely to be exactly the same—unlikely to be uniform. "
            "Choice A is incorrect. \"Neglected\" means suffering a lack of care, which doesn't apply. "
            "Choice B is incorrect. \"Redundant\" means not needed, which is too strong. "
            "Choice C is incorrect. \"Ongoing\" means still in progress, which makes no sense for a mineral distribution."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "99022257",
        "question_text": (
            "Archeological excavation of Market Street Chinatown, a nineteenth-century Chinese American community "
            "in San Jose, California, provided the first evidence that Asian food products were imported to the "
            "United States in the 1800s: bones from a freshwater fish species native to Southeast Asia. "
            "Jinshanzhuang—Hong Kong–based import/export firms—likely coordinated the fish's transport from "
            "Chinese-operated fisheries in Vietnam and Malaysia to North American markets. This route reveals "
            "the (often overlooked) multinational dimensions of the trade networks linking Chinese diaspora communities.\n\n"
            "Which choice best describes the function of the underlined sentence in the text as a whole?"
        ),
        "choices": [
            "A) It explains why efforts to determine the country of origin of the items mentioned in the previous sentence remain inconclusive.",
            "B) It provides information that helps support a claim about a discovery's significance that is presented in the following sentence.",
            "C) It traces the steps that were taken to locate and recover the objects that are described in the previous sentence.",
            "D) It outlines a hypothesis that additional evidence discussed in the following sentence casts some doubt on.",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. The underlined sentence provides information about import/export firms, "
            "showing how Chinese communities across the world were connected by trade routes, which supports the "
            "following sentence's claim about the multinational dimensions of those trade networks. "
            "Choice A is incorrect because the underlined sentence tells us exactly where the fish came from. "
            "Choice C is incorrect because the passage never describes the steps taken to discover the fish bones. "
            "Choice D is incorrect because the underlined sentence provides evidence, not a hypothesis, and the "
            "following sentence agrees with it rather than casting doubt on it."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "f0e70c0c",
        "question_text": (
            "The discoverers of the minor planet 1227 Geranium named it after the plant genus that includes "
            "cranesbills. Most of the recently discovered minor planets, however, are given only an identification "
            "number, largely due to there being over 500,000 such bodies known at present, which makes the already "
            "challenging task of finding a unique name for each nearly ______.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) insurmountable", "B) feasible", "C) substantial", "D) unnecessary"],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. \"Insurmountable\" means impossible to overcome or too difficult to solve. "
            "With over 500,000 known minor planets, finding unique names has become virtually impossible, which "
            "explains why most receive only identification numbers. "
            "Choice B is incorrect because \"feasible\" means possible to achieve, which would contradict the logic. "
            "Choice C is incorrect because \"substantial\" means considerable in size, which wouldn't logically explain "
            "why the naming practice was abandoned. "
            "Choice D is incorrect because \"unnecessary\" would suggest naming serves no purpose, but the text "
            "implies naming has value—it's just become impractical."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "fd7c6d0d",
        "question_text": (
            "The following text is from Charlotte Perkins Gilman's 1910 poem \"The Earth's Entail.\"\n\n"
            "No matter how we cultivate the land,\n"
            "Taming the forest and the prairie free;\n"
            "No matter how we irrigate the sand,\n"
            "Making the desert blossom at command,\n"
            "We must always leave the borders of the sea;\n"
            "The immeasureable reaches\n"
            "Of the windy wave-wet beaches,\n"
            "The million-mile-long margin of the sea.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) The speaker argues against interfering with nature and then gives evidence supporting this interference.",
            "B) The speaker presents an account of efforts to dominate nature and then cautions that such efforts are only temporary.",
            "C) The speaker provides examples of an admirable way of approaching nature and then challenges that approach.",
            "D) The speaker describes attempts to control nature and then offers a reminder that not all nature is controllable.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. In the first half, the speaker describes attempts to control nature: "
            "cultivating, taming, and irrigating different kinds of land. In the second half, the speaker states "
            "that we can never tame the sea or the beach. "
            "Choice A is incorrect because the speaker never argues that we should not interfere with nature. "
            "Choice B is incorrect because the speaker never describes our efforts as \"temporary.\" "
            "Choice C is incorrect because the speaker never describes the cultivation as \"admirable.\""
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "c4c7ef40",
        "question_text": (
            "In 2008 a complete set of ancient pessoi (glass game pieces) was uncovered from beneath a paving "
            "stone in modern-day Israel. Due to their small size, pessoi were easily misplaced, making a whole "
            "set a rare find. This has led some experts to suggest that the set may have been buried intentionally; "
            "however, without clear evidence, archaeologists are left to ______ what happened.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) speculate about", "B) dismiss", "C) expand on", "D) catalog"],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. \"Speculate\" means to form a theory or guess without clear evidence, "
            "which matches the context since archaeologists lack \"clear evidence\" about what happened. "
            "Choice B is incorrect. \"Dismiss\" means treat as unworthy of consideration; the archaeologists are "
            "trying to figure out the truth, not dismiss it. "
            "Choice C is incorrect. \"Expand on\" means give more details about, but without clear evidence "
            "there are no details to give. "
            "Choice D is incorrect. \"Catalog\" means carefully record, but there's no clear evidence to catalog."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "542fe6df",
        "question_text": (
            "The fossil remains of the individual known as Oase 1, discovered in Romania in 2002, can help "
            "paleoanthropologists not only ______ steps in the evolution of hominids but also illuminate the "
            "Pleistocene epoch generally, revealing important details about the time in which Oase 1 lived.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) exploit", "B) discern", "C) prioritize", "D) yield"],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. \"Discern\" means to detect or recognize something, especially something "
            "hidden or obscure. The Oase 1 fossil can help paleoanthropologists recognize patterns in the "
            "evolutionary process and gain insights into facts still not well understood. "
            "Choice A is incorrect. \"Exploit\" would suggest using steps in the evolution of hominids, which "
            "doesn't make logical sense. "
            "Choice C is incorrect. \"Prioritize\" would suggest placing more importance on certain steps or "
            "ordering them, which doesn't fit. "
            "Choice D is incorrect. To \"yield\" or generate steps in evolution doesn't make sense; researchers "
            "detect patterns, they don't create them."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "fdf8e5b3",
        "question_text": (
            "Text 1\nThe idea that time moves in only one direction is instinctively understood, yet it puzzles "
            "physicists. According to the second law of thermodynamics, at a macroscopic level some processes of "
            "heat transfer are irreversible due to the production of entropy—after a transfer we cannot rewind "
            "time and place molecules back exactly where they were before, just as we cannot unbreak dropped eggs. "
            "But laws of physics at a microscopic or quantum level hold that those processes should be reversible.\n\n"
            "Text 2\nIn 2015, physicists Tiago Batalhão et al. performed an experiment in which they confirmed "
            "the irreversibility of thermodynamic processes at a quantum level, producing entropy by applying a "
            "rapidly oscillating magnetic field to a system of carbon-13 atoms in liquid chloroform. But the "
            "experiment \"does not pinpoint ... what causes [irreversibility] at the microscopic level,\" "
            "coauthor Mauro Paternostro said.\n\n"
            "Based on the texts, what would the author of Text 1 most likely say about the experiment described in Text 2?"
        ),
        "choices": [
            "A) It would suggest an interesting direction for future research were it not the case that two of the physicists who conducted the experiment disagree on the significance of its findings.",
            "B) It provides empirical evidence that the current understanding of an aspect of physics at a microscopic level must be incomplete.",
            "C) It is consistent with the current understanding of physics at a microscopic level but not at a macroscopic level.",
            "D) It supports a claim about an isolated system of atoms in a laboratory, but that claim should not be extrapolated to a general claim about the universe.",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. Author 1 describes the puzzle that at a microscopic level the laws of "
            "physics suggest processes should be reversible. The experiment confirmed that those processes are "
            "not reversible even at the microscopic level but didn't explain why. This supports Author 1's point "
            "that physicists still don't fully understand how things work at a microscopic level. "
            "Choice A is incorrect because Text 2 never suggests that two physicists disagree on the findings. "
            "Choice C is incorrect because the experiment confirmed the macroscopic-level law was still true at "
            "the microscopic level, supporting the macroscopic understanding. "
            "Choice D is incorrect because neither text makes a distinction between laboratory findings and "
            "the way the universe works in general."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "815b354f",
        "question_text": (
            "Using NASA's powerful James Webb Space Telescope (JWST), Mercedes López-Morales and colleagues "
            "measured the wavelengths of light traveling through the atmosphere of WASP-39b, an exoplanet, or "
            "planet outside our solar system. Different molecules absorb different wavelengths of light, and the "
            "wavelength measurements showed the presence of carbon dioxide (CO2) in WASP-39b's atmosphere. This "
            "finding not only offers the first decisive evidence of CO2 in the atmosphere of an exoplanet but also "
            "illustrates the potential for future scientific breakthroughs held by the JWST.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) It discusses a method used by some researchers, then states why an alternative method is superior to it.",
            "B) It describes how researchers made a scientific discovery, then explains the importance of that discovery.",
            "C) It outlines the steps taken in a scientific study, then presents a hypothesis based on that study.",
            "D) It examines how a group of scientists reached a conclusion, then shows how other scientists have challenged that conclusion.",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. The text begins by describing how researchers used the JWST to detect "
            "CO2 in WASP-39b's atmosphere. Then it discusses the significance of this finding as the first evidence "
            "of CO2 in an exoplanet's atmosphere and as an illustration of the JWST's potential. "
            "Choice A is incorrect because the text doesn't compare two different methods. "
            "Choice C is incorrect because the text doesn't present a hypothesis but reports findings. "
            "Choice D is incorrect because no scientists challenging the conclusion are mentioned."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "720b79de",
        "question_text": (
            "In the Here and Now Storybook (1921), educator Lucy Sprague Mitchell advanced the then controversial "
            "idea that books for very young children should imitate how they use language, since toddlers, who "
            "cannot yet grasp narrative or abstract ideas, seek reassurance in verbal repetition and naming. The "
            "most enduring example of this idea is Margaret Wise Brown's 1947 picture book Goodnight Moon, in "
            "which a young rabbit names the objects in his room as he drifts off to sleep. Scholars note that the "
            "book's emphasis on repetition, rhythm, and nonsense rhyme speaks directly to Mitchell's influence.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) The text outlines a debate between two authors of children's literature and then traces how that debate shaped theories on early childhood education.",
            "B) The text summarizes an argument about how children's literature should be evaluated and then discusses a contrasting view on that subject.",
            "C) The text lists the literary characteristics that are common to many classics of children's literature and then indicates the narrative subjects that are most appropriate for young children.",
            "D) The text presents a philosophy about what material is most suitable for children's literature and then describes a book influenced by that philosophy.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The text starts by introducing Mitchell's philosophy about using simple, "
            "repetitive language in books for young children. Then it describes Goodnight Moon, a book influenced "
            "by that philosophy. "
            "Choice A is incorrect because the two authors mentioned both agree about the type of language that "
            "should be in books for young children. "
            "Choice B is incorrect because the text never introduces a competing view. "
            "Choice C is incorrect because the text doesn't discuss many classics—it describes one educational "
            "theory and one example."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "48b6c74f",
        "question_text": (
            "The following text is adapted from Nathaniel Hawthorne's 1837 story \"Dr. Heidegger's Experiment.\" "
            "The main character, a physician, is experimenting with rehydrating a dried flower.\n\n"
            "At first [the rose] lay lightly on the surface of the fluid, appearing to imbibe none of its moisture. "
            "Soon, however, a singular change began to be visible. The crushed and dried petals stirred and assumed "
            "a deepening tinge of crimson, as if the flower were reviving from a deathlike slumber.\n\n"
            'As used in the text, what does the phrase "a singular" most nearly mean?'
        ),
        "choices": ["A) A lonely", "B) A disagreeable", "C) An acceptable", "D) An extraordinary"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer because \"singular\" most nearly means extraordinary. The rose undergoes "
            "an exceptional transformation—its color deepens and it revives \"from a deathlike slumber\"—an "
            "extraordinary change. "
            "Choice A is incorrect because in this context \"singular\" doesn't imply loneliness. "
            "Choice B is incorrect because \"singular\" has no meaning related to being disagreeable. "
            "Choice C is incorrect because \"singular\" means extraordinary, not merely acceptable."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "cc00a8cf",
        "question_text": (
            "Works of moral philosophy, such as Plato's Republic or Aristotle's Nicomachean Ethics, are partly "
            "concerned with how to live a morally good life. But philosopher Jonathan Barnes argues that works "
            "that present a method of living such a life without also supplying a motive are inherently useful "
            "only to those already wishing to be morally good—those with no desire for moral goodness will not "
            "choose to follow their rules. However, some works of moral philosophy attempt to describe what "
            "constitutes a morally good life while also proposing reasons for living one.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) It provides a characterization about a field of thought by noting two works in it and then details a way in which some works in that field are more comprehensive than others.",
            "B) It mentions two renowned works and then claims that despite their popularity it is impossible for these works to serve the purpose their authors intended.",
            "C) It summarizes the history of a field of thought by discussing two works and then proposes a topic of further research for specialists in that field.",
            "D) It describes two influential works and then explains why one is more widely read than the other.",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. The text starts by stating what moral philosophy is concerned with and "
            "naming two examples. Then it describes a shortcoming of some works (they say how but not why), and "
            "finally states that other works include both how and why. "
            "Choice B is incorrect because the text never argues these works don't serve their intended purpose. "
            "Choice C is incorrect because the text never discusses the history of moral philosophy or proposes "
            "further research. "
            "Choice D is incorrect because the text never discusses which of the two works is more widely read."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "cf6f36e3",
        "question_text": (
            "Like the 1945 play it reimagines—Federico García Lorca's The House of Bernarda Alba—Marcus Gardley's "
            "2014 play The House That Will Not Stand prominently features women. In both plays, the all-female "
            "cast ______ an array of female characters, including a strong mother and several daughters dealing "
            "with individual struggles.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) engulfs", "B) encourages", "C) comprises", "D) provokes"],
        "correct_answer": "C",
        "explanation": (
            "Choice C is the best answer. \"Comprises\" means constitutes or makes up the totality of. Because "
            "all cast members are female, the cast constitutes, or comprises, the collection of characters. "
            "Choice A is incorrect. \"Engulfs\" would mean encloses or overwhelms, which doesn't fit. "
            "Choice B is incorrect. \"Encourages\" would mean inspires with courage, which doesn't make sense "
            "in describing the relationship between cast and characters. "
            "Choice D is incorrect. \"Provokes\" would mean incites to anger, which doesn't apply."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "893975a3",
        "question_text": (
            "The following text is adapted from Zora Neale Hurston's 1921 short story \"John Redding Goes to Sea.\" "
            "John wants to travel far beyond the village where he lives near his mother, Matty.\n\n"
            "[John] had on several occasions attempted to reconcile his mother to the notion, but found it a "
            "difficult task. Matty always took refuge in self-pity and tears. Her son's desires were "
            "incomprehensible to her, that was all.\n\n"
            'As used in the text, what does the phrase "reconcile his mother to" most nearly mean?'
        ),
        "choices": [
            "A) Get his mother to accept",
            "B) Get his mother to apologize for",
            "C) Get his mother to match",
            "D) Get his mother to reunite with",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. \"Reconcile to\" means to cause a person to accept something difficult "
            "or disagreeable. John wants his mother to accept his desire to travel, even though she doesn't like it. "
            "Choice B is incorrect. John doesn't want his mother to apologize for his desire to travel. "
            "Choice C is incorrect. The text doesn't suggest John wants his mother to match his desire to travel. "
            "Choice D is incorrect. It would be strange to say that a person \"reunites with\" a notion."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "6989e0f9",
        "question_text": (
            "The following text is adapted from Nathaniel Hawthorne's 1844 short story \"Drowne's Wooden Image.\" "
            "Drowne, a young man, is carving a wooden figure to decorate the front of a ship.\n\n"
            "Day by day, the work assumed greater precision, and settled its irregular and misty outline into "
            "distincter grace and beauty. The general design was now obvious to the common eye.\n\n"
            'As used in the text, what does the word "assumed" most nearly mean?'
        ),
        "choices": ["A) Acquired", "B) Acknowledged", "C) Imitated", "D) Speculated"],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. \"Assumed\" most nearly means acquired, or came to possess. As Drowne "
            "continued to carve, the wooden object came to possess greater precision, changing from an indistinct "
            "outline into a graceful, recognizable form. "
            "Choice B is incorrect because an inanimate object like the wooden figure can't acknowledge its own "
            "precision. "
            "Choice C is incorrect because there's nothing to suggest the figure merely imitated precision—it "
            "gradually became more precise. "
            "Choice D is incorrect because an inanimate object can't speculate about its own precision."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "c5766314",
        "question_text": (
            "The Illustrated History of San Mateo County, published in 1878, features several illustrations by "
            "Grafton Tyler Brown showing the California county's farms, residences, and businesses. It was ______ "
            "for a business to be featured, since being included suggested that a business was an important part "
            "of the community.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) risky", "B) misleading", "C) advantageous", "D) unremarkable"],
        "correct_answer": "C",
        "explanation": (
            "Choice C is the best answer. \"Advantageous\" means beneficial or providing a favorable position. "
            "Being included suggested importance within the community, which would benefit a business. "
            "Choice A is incorrect because \"risky\" would suggest negative consequences, but the text implies "
            "only positive outcomes. "
            "Choice B is incorrect because \"misleading\" would mean deceptive, which the text doesn't suggest. "
            "Choice D is incorrect because \"unremarkable\" means common or ordinary, but inclusion conferred "
            "special status."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "5b71d7b1",
        "question_text": (
            "In 1973, poet Miguel Algarín started inviting other writers who, like him, were Nuyorican—a term "
            "for New Yorkers of Puerto Rican heritage—to gather in his apartment to present their work. The "
            "gatherings were so well attended that Algarín soon had to rent space in a cafe to accommodate them. "
            "Thus, the Nuyorican Poets Cafe was born. Moving to a permanent location in 1981, the Nuyorican "
            "Poets Cafe expanded its original scope beyond the written word, hosting art exhibitions and musical "
            "performances as well. Half a century since its inception, it continues to foster emerging Nuyorican "
            "talent.\n\n"
            "Which choice best describes the overall purpose of the text?"
        ),
        "choices": [
            "A) To explain what motivated Algarín to found the Nuyorican Poets Cafe",
            "B) To situate the Nuyorican Poets Cafe within the cultural life of New York as a whole",
            "C) To discuss why the Nuyorican Poets Cafe expanded its scope to include art and music",
            "D) To provide an overview of the founding and mission of the Nuyorican Poets Cafe",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The text presents a brief history of the Nuyorican Poets Cafe, from "
            "how it got started in the '70s, to its expansion in the '80s, to its ongoing mission today. "
            "Choice A is incorrect because the text never mentions Algarín's motivations. "
            "Choice B is incorrect because the text never discusses the cultural life of New York as a whole. "
            "Choice C is incorrect because this is too narrow—the expansion is only one point in the broader history."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "cb771ec1",
        "question_text": (
            "Business researcher Melanie Brucks and colleagues found that remote video conference meetings may "
            "be less conducive to brainstorming than in-person meetings are. The researchers suspect that video "
            "meeting participants are focused on staring at the speaker on the screen and don't allow their eyes "
            "or mind to wander as much, which may ultimately ______ creativity.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) recommend", "B) criticize", "C) impede", "D) construct"],
        "correct_answer": "C",
        "explanation": (
            "Choice C is the best answer. Video meetings are \"less conducive to\" brainstorming, suggesting the "
            "participants' focus is bad for creativity. \"Impede\" means delay or prevent, which fits. "
            "Choice A is incorrect because \"recommend\" is too positive to fit the context. "
            "Choice B is incorrect because it wouldn't make sense to say that over-focusing \"criticizes\" creativity. "
            "Choice D is incorrect because \"construct\" means build or make, which is too positive."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "925e4e31",
        "question_text": (
            "Text 1\nPolar bears sustain themselves primarily by hunting seals on the Arctic sea ice, but rising "
            "ocean temperatures are causing the ice to diminish, raising concerns about polar bear population "
            "declines as these large predators' seal-hunting habitats continue to shrink. A 2020 study examining "
            "polar bear populations across the Arctic concluded that populations affected by sea-ice loss are at "
            "great risk of extinction by the end of the twenty-first century.\n\n"
            "Text 2\nMonitoring carried out by researchers from the Norwegian Polar Institute shows that the polar "
            "bear population on the Arctic archipelago of Svalbard remains stable and well nourished despite "
            "rapidly declining sea ice in recent years. The researchers attribute this population's resilience in "
            "part to a shift in feeding strategies: in addition to hunting seals, the Svalbard polar bears have "
            "begun relying on a diet of reindeer meat and birds' eggs.\n\n"
            "Based on the texts, how would the researchers in Text 2 most likely respond to the conclusion "
            "presented in the underlined portion of Text 1?"
        ),
        "choices": [
            "A) By noting that it neglects the possibility of some polar bear populations adapting to changes in their environment",
            "B) By suggesting that it is likely incorrect about the rates at which warming ocean temperatures have caused sea ice to melt in the Arctic",
            "C) By asserting that it overlooks polar bear populations that have not yet been affected by loss of seal-hunting habitats",
            "D) By arguing that it fails to account for polar bears' reliance on a single seal-hunting strategy",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. Text 2 describes how the Svalbard polar bears have adapted to the loss "
            "of sea ice by diversifying their diet, remaining \"stable and well nourished.\" This counters the "
            "claim that polar bears facing sea-ice loss are at \"great risk of extinction.\" "
            "Choice B is incorrect because Text 2 does not challenge the fact that sea ice is rapidly declining. "
            "Choice C is incorrect because Text 2 focuses on a population that has been affected by sea-ice loss "
            "but has survived, not unaffected populations. "
            "Choice D is incorrect because Text 2 would say Text 1 fails to account for polar bears' ability to "
            "develop other food sources, not their reliance on a single strategy."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "d6b84972",
        "question_text": (
            "The following text is from Joseph Conrad's 1907 novel The Secret Agent: A Simple Tale. Mr. Verloc "
            "is navigating the London streets on his way to a meeting.\n\n"
            "Before reaching Knightsbridge, Mr. Verloc took a turn to the left out of the busy main thoroughfare, "
            "uproarious with the traffic of swaying omnibuses and trotting vans, in the almost silent, swift flow "
            "of hansoms [horse-drawn carriages]. Under his hat, worn with a slight backward tilt, his hair had "
            "been carefully brushed into respectful sleekness; for his business was with an Embassy. And Mr. "
            "Verloc, steady like a rock—a soft kind of rock—marched now along a street which could with every "
            "propriety be described as private.\n\n"
            "Which choice best describes the function of the underlined phrase in the text as a whole?"
        ),
        "choices": [
            "A) It qualifies an earlier description of Mr. Verloc.",
            "B) It emphasizes an internal struggle Mr. Verloc experiences.",
            "C) It contrasts Mr. Verloc with his surroundings.",
            "D) It reveals a private opinion Mr. Verloc holds.",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. The underlined phrase qualifies (adds limits or conditions to) the "
            "description of Mr. Verloc as \"steady like a rock,\" adding that he is a \"soft\" rock. "
            "Choice B is incorrect because the passage never mentions Mr. Verloc experiencing any internal struggles. "
            "Choice C is incorrect because the underlined phrase modifies the description of him as a rock, "
            "not contrasting him with his surroundings. "
            "Choice D is incorrect because the underlined phrase further describes his character for the reader, "
            "not a private opinion he holds."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "014ae202",
        "question_text": (
            "The following text is adapted from Charles Dickens's 1854 novel Hard Times. Coketown is a fictional "
            "town in England.\n\n"
            "[Coketown] contained several large streets all very like one another, and many small streets still "
            "more like one another, inhabited by people equally like one another, who all went in and out at the "
            "same hours, with the same sound upon the same pavements, to do the same work, and to whom every day "
            "was the same as yesterday and tomorrow, and every year the counterpart of the last and the next.\n\n"
            "Which choice best states the main purpose of the text?"
        ),
        "choices": [
            "A) To emphasize the uniformity of both the town and the people who live there",
            "B) To explain the limited work opportunities available to the town's residents",
            "C) To reveal how the predictability of the town makes it easy for people lose track of time",
            "D) To argue that the simplicity of life in the town makes it a pleasant place to live",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. The author describes Coketown as having streets that are all very similar "
            "and residents who live similarly and do the same work. The repetition of similarities emphasizes how "
            "everything in Coketown is alike. "
            "Choice B is incorrect because the text mentions that residents \"do the same work\" but never explains "
            "what that work is or why everyone does it. "
            "Choice C is incorrect because the text never suggests that people actually \"lose track of time.\" "
            "Choice D is incorrect because the text never mentions whether life is simple, and the town sounds "
            "dull rather than pleasant."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "ad1fc529",
        "question_text": (
            "Interruptions in the supply chain for microchips used in personal electronics have challenged an "
            "economist's assertion that retailers can expect robust growth in sales of those devices in the coming "
            "months. The delays are unlikely to ______ her projection entirely but will almost certainly extend "
            "its time frame.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) dispute", "B) withdraw", "C) underscore", "D) invalidate"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. \"Invalidate\" means nullify or make invalid. The delays will extend "
            "the time frame but are unlikely to nullify the projection entirely. "
            "Choice A is incorrect because delays, as an inanimate circumstance, can't \"dispute\" or argue against "
            "a prediction. "
            "Choice B is incorrect because the delays themselves can't \"withdraw\" (remove from consideration) "
            "the projection. "
            "Choice C is incorrect because there's nothing to suggest the delays will \"underscore\" or emphasize "
            "the projection."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "d3fe0b12",
        "question_text": (
            "The following text is adapted from Etsu Inagaki Sugimoto's 1925 memoir A Daughter of the Samurai. "
            "As a young woman, Sugimoto moved from feudal Japan to the United States.\n\n"
            "The standards of my own and my adopted country differed so widely in some ways, and my love for "
            "both lands was so sincere, that sometimes I had an odd feeling of standing upon a cloud in space, "
            "and gazing with measuring eyes upon two separate worlds. At first I was continually trying to "
            "explain, by Japanese standards, all the queer things that came every day before my surprised eyes; "
            "for no one seemed to know the origin or significance of even the most familiar customs, nor why "
            "they existed and were followed.\n\n"
            "Which choice best describes the main purpose of the text?"
        ),
        "choices": [
            "A) To convey the narrator's experience of observing and making sense of differences between two cultures she embraces",
            "B) To establish the narrator's hope of forming connections with new companions by sharing customs she learned as a child",
            "C) To reveal the narrator's recognition that she is hesitant to ask questions about certain aspects of a culture she is newly encountering",
            "D) To emphasize the narrator's wonder at discovering that the physical distance between two countries is greater than she had expected",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. The narrator loves both her native Japan and adopted United States, and "
            "she initially used Japanese standards to explain unfamiliar American experiences. The main purpose "
            "is to convey her experience of observing and making sense of differences between two cultures she "
            "embraces. "
            "Choice B is incorrect because the text makes no reference to possible companions. "
            "Choice C is incorrect because nothing suggests the narrator was hesitant to ask questions—in fact, "
            "\"no one seemed to know\" suggests she asked. "
            "Choice D is incorrect because the text makes no reference to physical distance between countries."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "5cc62890",
        "question_text": (
            "Text 1\nThe live music festival business is growing in event size and genre variety. With so many "
            "consumer options, organizers are finding ways to cement festival attendance as a special experience "
            "worth sharing. This phenomenon is linked to the growing \"experiential economy,\" where many find "
            "it gratifying to purchase lived experiences. To ensure a profitable event, venues need to consider "
            "the overall consumer experience, not just the band lineup.\n\n"
            "Text 2\nMusic festival appearances are becoming a more important part of musicians' careers. One "
            "factor in this shift is the rising use of streaming services that allow access to huge numbers of "
            "songs for a monthly fee, subsequently reducing sales of full-length albums. With this shift in "
            "consumer behavior, musicians are increasingly dependent on revenue from live performances.\n\n"
            "Based on the texts, both authors would most likely agree with which statement?"
        ),
        "choices": [
            "A) Consumers are more interested in paying subscription fees to stream music than in attending music festivals in person.",
            "B) Consumers' growing interest in purchasing experiences is mostly confined to the music industry.",
            "C) Changing consumer behaviors are leading to changes in music-related businesses.",
            "D) The rising consumer demand for live music festivals also generates higher demand for music streaming platforms.",
        ],
        "correct_answer": "C",
        "explanation": (
            "Choice C is the best answer. Both authors mention how consumer behaviors have shifted and how this "
            "affects the music industry. Text 1: consumers enjoy purchasing \"lived experiences,\" influencing "
            "how organizers design festivals. Text 2: consumers use streaming more, reducing album sales and "
            "increasing the importance of live performances. "
            "Choice A is incorrect because neither text claims consumers prefer streaming over festivals. "
            "Choice B is incorrect because Text 1 identifies music festivals as just one example of the broader "
            "\"experiential economy\" trend. "
            "Choice D is incorrect because neither text establishes a cause/effect relationship between festival "
            "demand and streaming demand."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "b99e3267",
        "question_text": (
            "A journalist and well-respected art critic of nineteenth-century Britain, Lady Elizabeth Rigby "
            "Eastlake did not hesitate to publish reviews that went against popular opinion. One of her most "
            "divisive works was an essay questioning the idea of photography as an emerging medium for fine art: "
            "in the essay, Eastlake ______ that the value of photographs was informational rather than creative.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) exposed", "B) asserted", "C) discovered", "D) doubted"],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. \"Asserted\" means stated confidently. Eastlake \"did not hesitate to "
            "publish reviews going against popular opinion,\" so she was confident in sharing her opinions. "
            "Choice A is incorrect. \"Exposed\" means made visible by uncovering a truth; Eastlake was sharing "
            "an opinion, not uncovering a truth. "
            "Choice C is incorrect. \"Discovered\" means found, but Eastlake was writing her own opinion. "
            "Choice D is incorrect. \"Doubted\" means didn't believe in; placing \"doubted\" in the blank would "
            "suggest the opposite of what she believes."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "d87c4362",
        "question_text": (
            "Drivers who strongly believe that the toll they must pay to use the Lewis and Clark Bridge, which "
            "spans the Ohio River to connect Indiana and Kentucky, is currently too high are unlikely to be ______ "
            "a proposal to increase the toll. Advocates for a higher toll are likely to have more success if they "
            "instead direct their arguments toward a more persuadable segment of the population.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) receptive to", "B) apprised of", "C) incensed by", "D) cited in"],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. \"Receptive to\" means open to or willing to consider something. "
            "Drivers who already think the toll is too high are not persuadable—they are unlikely to be willing "
            "to consider a toll increase proposal. "
            "Choice B is incorrect because \"apprised of\" means informed about, and nothing suggests these "
            "drivers wouldn't be informed of the proposal. "
            "Choice C is incorrect because drivers who think the toll is already too high likely would be angered "
            "by a proposal to raise it, so saying they are \"unlikely to be incensed\" doesn't make sense. "
            "Choice D is incorrect because \"cited in\" means referred to in something, which doesn't fit the context."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "f3a51fa6",
        "question_text": (
            "Horizontal gene transfer occurs when an organism of one species acquires genetic material from an "
            "organism of another species through nonreproductive means. The genetic material can then be "
            "transferred \"vertically\" in the second species—that is, through reproductive inheritance. Scientist "
            "Atma Ivancevic and her team have hypothesized infection by invertebrate parasites as a mechanism of "
            "horizontal gene transfer between vertebrate species: while feeding, a parasite could acquire a gene "
            "from one host, then relocate to a host from a different vertebrate species and transfer the gene to "
            "it in turn.\n\n"
            "Which choice best describes the function of the underlined portion in the text as a whole?"
        ),
        "choices": [
            "A) It explains why parasites are less susceptible to horizontal gene transfer than their hosts are.",
            "B) It clarifies why some genes are more likely to be transferred horizontally than others are.",
            "C) It contrasts how horizontal gene transfer occurs among vertebrates with how it occurs among invertebrates.",
            "D) It describes a means by which horizontal gene transfer might occur among vertebrates.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The text defines horizontal gene transfer and gives one possibility for "
            "how it happens in vertebrates (via infection by parasites). The underlined part describes how that "
            "mechanism could work. "
            "Choice A is incorrect because parasites are described as the mechanism that does the transferring, "
            "not the species that gives or receives genes. "
            "Choice B is incorrect because the text never discusses which genes are more likely to be transferred. "
            "Choice C is incorrect because the text never discusses how horizontal gene transfer occurs among invertebrates."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "e08dee38",
        "question_text": (
            "In Nature Poem (2017), Kumeyaay poet Tommy Pico portrays his ______ the natural world by honoring "
            "the centrality of nature within his tribe's traditional beliefs while simultaneously expressing his "
            "distaste for being in wilderness settings himself.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": [
            "A) responsiveness to",
            "B) ambivalence toward",
            "C) renunciation of",
            "D) mastery over",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. \"Ambivalence toward\" means mixed feelings about. Pico honors the "
            "centrality of nature in his tribe's beliefs but also expresses distaste for being in wilderness "
            "settings—mixed feelings about the natural world. "
            "Choice A is incorrect because \"responsiveness to\" means quick to react to, which isn't supported "
            "by the text. "
            "Choice C is incorrect because \"renunciation of\" means rejecting, but the text shows both positive "
            "and negative responses, not rejection. "
            "Choice D is incorrect because \"mastery over\" means having control over, which isn't supported."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "77d93b6f",
        "question_text": (
            "Text 1\nMany studies in psychology have shown that people seek out information even when they know "
            "in advance that they have no immediate use for it and that they won't directly benefit from it. Such "
            "findings support the consensus view among researchers of curiosity: namely, that curiosity is not "
            "instrumental but instead represents a drive to acquire information for its own sake.\n\n"
            "Text 2\nWhile acknowledging that acquiring information is a powerful motivator, Rachit Dubey and "
            "colleagues ran an experiment to test whether emphasizing the usefulness of scientific information "
            "could increase curiosity about it. They found that when research involving rats and fruit flies was "
            "presented as having medical applications for humans, participants expressed greater interest in "
            "learning about it than when the research was not presented as useful.\n\n"
            "Based on the texts, how would Dubey and colleagues (Text 2) most likely respond to the consensus "
            "view discussed in Text 1?"
        ),
        "choices": [
            "A) By suggesting that curiosity may not be exclusively motivated by the desire to merely acquire information",
            "B) By conceding that people may seek out information that serves no immediate purpose only because they think they can use it later",
            "C) By pointing out that it is challenging to determine when information-seeking serves no goal beyond acquiring information",
            "D) By disputing the idea that curiosity can help explain apparently purposeless information-seeking behaviors",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. The researchers in Text 2 recognize that acquiring information is a "
            "powerful motivator, but showed that this motivation can be affected by other factors—like whether the "
            "information is expected to be useful. This suggests other desires may play a part in driving "
            "information acquisition. "
            "Choice B is incorrect because the consensus view in Text 1 is that people acquire information "
            "regardless of whether they think they can use it later; Dubey and colleagues acknowledge this. "
            "Choice C is incorrect because neither text discusses the difficulty of determining the motivation "
            "for information-seeking. "
            "Choice D is incorrect because Text 2 starts with Dubey and colleagues acknowledging that curiosity "
            "is a powerful motivator."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "5405400f",
        "question_text": (
            "The following text is from Herman Melville's 1854 novel The Lightning-rod Man.\n\n"
            "The stranger still stood in the exact middle of the cottage, where he had first planted himself. "
            "His singularity impelled a closer scrutiny. A lean, gloomy figure. Hair dark and lank, mattedly "
            "streaked over his brow. His sunken pitfalls of eyes were ringed by indigo halos, and played with "
            "an innocuous sort of lightning: the gleam without the bolt. The whole man was dripping. He stood "
            "in a puddle on the bare oak floor: his strange walking-stick vertically resting at his side.\n\n"
            "Which choice best states the function of the underlined sentence in the overall structure of the text?"
        ),
        "choices": [
            "A) It elaborates on the previous sentence's description of the character.",
            "B) It introduces the setting that is described in the sentences that follow.",
            "C) It establishes a contrast with the description in the previous sentence.",
            "D) It sets up the character description presented in the sentences that follow.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The underlined sentence says \"He stood out, so I looked more closely "
            "at him.\" Then the rest of the text describes him in detail. "
            "Choice A is incorrect because the previous sentence says \"He was still standing in the middle of "
            "the cottage\"—it doesn't include any description of the character himself. "
            "Choice B is incorrect because the following sentences describe the character, not the setting. "
            "Choice C is incorrect because there's no contrast between the underlined sentence and the previous one."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "b662c384",
        "question_text": (
            "The following text is adapted from Upton Sinclair's 1906 novel The Jungle. Marija is helping to "
            "manage her sister's wedding.\n\n"
            "It was [Marija's] task to see that all things went in due form, and after the best home traditions; "
            "and, flying wildly hither and thither, bowling every one out of the way, and scolding and exhorting "
            "all day with her tremendous voice, Marija was too eager to see that others conformed to the "
            "proprieties to consider them herself.\n\n"
            'As used in the text, what does the word "consider" most nearly mean?'
        ),
        "choices": [
            "A) Take into account and follow",
            "B) Admire steadily and praise",
            "C) Come to a decision about",
            "D) Have an opinion on",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. \"Consider\" most nearly means to take into account and follow. Marija "
            "was so focused on ensuring others conformed to the proprieties that she failed to take those standards "
            "into account and follow them herself. "
            "Choice B is incorrect because the text doesn't suggest Marija failed to admire and praise the proprieties. "
            "Choice C is incorrect because the text doesn't suggest Marija was unable to make a decision about "
            "the proprieties—she knew very clearly which behaviors were appropriate. "
            "Choice D is incorrect because the text conveys that Marija had strong feelings about which behaviors "
            "were proper."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "684132cd",
        "question_text": (
            "The following text is adapted from George Eliot's 1857 short story \"The Sad Fortunes of the Rev. "
            "Amos Barton.\" Mr. Ely is a clergyman in the town of Milby.\n\n"
            "By the laity of Milby and its neighbourhood [Mr. Ely] was regarded as a man of quite remarkable "
            "powers and learning, who must make a considerable sensation in London pulpits and drawing-rooms on "
            "his occasional visit to the metropolis; and by his brother clergy he was regarded as a discreet and "
            "agreeable fellow. Mr. Ely never got into a warm discussion; he suggested what might be thought, but "
            "rarely said what he thought himself; he never let either men or women see that he was laughing at "
            "them, and he never gave any one an opportunity of laughing at him.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) It shows that Mr. Ely had originally been held in high regard by his friends and then details the events that caused their regard for him to subside.",
            "B) It implies that Mr. Ely's neighbors are more naïve in their estimation of him than people in London are and then explains why his neighbors have been so easily misled.",
            "C) It stresses the discrepancy between Mr. Ely's public and private conduct and then alludes to his motivation for hiding his true personality.",
            "D) It presents the favorable opinion of Mr. Ely that other people hold and then describes the behaviors of Mr. Ely that enable him to maintain that favorable opinion.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The first part presents the favorable opinions others hold of Mr. Ely: "
            "the laity regard him as having \"remarkable powers and learning\" and his clergy see him as \"discreet "
            "and agreeable.\" The text then describes Mr. Ely's behaviors that enable him to cultivate this "
            "positive reputation—avoiding confrontations, not revealing his true thoughts, not ridiculing anyone. "
            "Choice A is incorrect because the text doesn't describe any events that caused people's regard for "
            "Mr. Ely to diminish. "
            "Choice B is incorrect because the text doesn't suggest Mr. Ely's neighbors are more naïve than Londoners. "
            "Choice C is incorrect because the text doesn't discuss Mr. Ely's private conduct at all."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "cd742fda",
        "question_text": (
            "Michelene Pesantubbee, a historian and citizen of the Choctaw Nation, has identified a dilemma "
            "inherent to research on the status of women in her tribe during the 1600s and 1700s: the primary "
            "sources from that era, travel narratives and other accounts by male European colonizers, underestimate "
            "the degree of power conferred on Choctaw women by their traditional roles in political, civic, and "
            "ceremonial life. Pesantubbee argues that the Choctaw oral tradition and findings from archaeological "
            "sites in the tribe's homeland supplement the written record by providing crucial insights into those "
            "roles.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) It details the shortcomings of certain historical sources, then argues that research should avoid those sources altogether.",
            "B) It describes a problem that arises in research on a particular topic, then sketches a historian's approach to addressing that problem.",
            "C) It lists the advantages of a particular research method, then acknowledges a historian's criticism of that method.",
            "D) It characterizes a particular topic as especially challenging to research, then suggests a related topic for historians to pursue instead.",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. The text begins by stating a problem: written primary sources underestimate "
            "the power Choctaw women had. Then it presents one historian's solution: looking to oral tradition and "
            "archaeological findings for more insight. "
            "Choice A is incorrect because the text never says research should avoid written primary sources. "
            "Choice C is incorrect because the text never mentions the advantages of using written primary sources. "
            "Choice D is incorrect because the text never suggests the topic is too challenging or proposes "
            "an alternative topic."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "f242d54d",
        "question_text": (
            "Many archaeologists assume that large-scale engineering projects in ancient societies required an "
            "elite class to plan and direct the necessary labor. However, recent discoveries, such as the "
            "excavation of an ancient canal near the Gulf Coast of Alabama, have complicated this picture. Using "
            "radiocarbon dating, a team of researchers concluded that the 1.39-kilometer-long canal was most "
            "likely constructed between 576 and 650 CE by an Indigenous society that was relatively free of "
            "social classes.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) It describes a common view among archaeologists, then discusses a recent finding that challenges that view.",
            "B) It outlines a method used in some archaeological fieldwork, then explains why an alternative method is superior to it.",
            "C) It presents contradictory conclusions drawn by archaeologists, then evaluates a study that has apparently resolved that contradiction.",
            "D) It identifies a gap in scientific research, then presents a strategy used by some archaeologists to remedy that gap.",
        ],
        "correct_answer": "A",
        "explanation": (
            "Choice A is the best answer. The text starts by introducing a common view about the need for an "
            "elite class to direct large-scale engineering projects. Then it discusses a canal most likely built "
            "by a society without an elite class, challenging that view. "
            "Choice B is incorrect because the text discusses carbon dating as a method but doesn't compare it "
            "to any alternative methods. "
            "Choice C is incorrect because the study introduces a contradiction rather than resolving one. "
            "Choice D is incorrect because the text never identifies any gaps in scientific research."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "ba3ddf3b",
        "question_text": (
            "Text 1\nBecause literacy in Nahuatl script, the writing system of the Aztec Empire, was lost after "
            "Spain invaded central Mexico in the 1500s, it is unclear exactly how meaning was encoded in the "
            "script's symbols. Although many scholars had assumed that the symbols signified entire words, "
            "linguist Alfonso Lacadena theorized in 2008 that they signified units of language smaller than "
            "words: individual syllables.\n\n"
            "Text 2\nThe growing consensus among scholars of Nahuatl script is that many of its symbols could "
            "signify either words or syllables, depending on syntax and content at any given site within a text. "
            "For example, the symbol signifying the word huipil (blouse) in some contexts could signify the "
            "syllable \"pil\" in others, as in the place name \"Chipiltepec.\" Thus, for the Aztecs, reading "
            "required a determination of how such symbols functioned each time they appeared in a text.\n\n"
            "Based on the texts, how would the author of Text 2 most likely characterize Lacadena's theory, "
            "as described in Text 1?"
        ),
        "choices": [
            "A) By praising the theory for recognizing that the script's symbols could represent entire words",
            "B) By arguing that the theory is overly influenced by the work of earlier scholars",
            "C) By approving of the theory's emphasis on how the script changed over time",
            "D) By cautioning that the theory overlooks certain important aspects of how the script functioned",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. Lacadena's theory is that Nahuatl script symbols signified syllables, "
            "but the consensus described in Text 2 is that they can signify either words or syllables depending "
            "on context. The author of Text 2 would consider Lacadena's theory too simplistic: it's missing "
            "the importance of context in determining the meaning of a symbol. "
            "Choice A is incorrect because Lacadena's theory is that symbols signified syllables, not words. "
            "Choice B is incorrect because Text 1 states that Lacadena's theory differed from what earlier "
            "scholars believed. "
            "Choice C is incorrect because neither text mentions how or if the script changed over time."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "8a4a2079",
        "question_text": (
            "Novelist N. K. Jemisin declines to ______ the conventions of the science fiction genre in which "
            "she writes, and she has suggested that her readers appreciate her work precisely because of this "
            "willingness to thwart expectations and avoid formulaic plots and themes.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) question", "B) react to", "C) perceive", "D) conform to"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. \"Conform to\" means to act in accordance with something. Jemisin "
            "declines to act in accordance with the conventions of the genre, choosing instead to thwart "
            "expectations and avoid formulaic plots. "
            "Choice A is incorrect. \"Question\" would mean doubt or object to; the text suggests Jemisin may "
            "actually object to the conventions, not that she chooses not to question them. "
            "Choice B is incorrect. The text indicates Jemisin is acting in response to conventions by "
            "deliberately avoiding them, not declining to react. "
            "Choice C is incorrect. \"Perceive\" would mean become aware of; Jemisin is clearly aware of the "
            "conventions and deliberately avoids them."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "ec66fe4d",
        "question_text": (
            "To develop a method for measuring snow depth with laser beams, NASA physicist Yongxiang Hu relied "
            "on ______; identifying broad similarities between two seemingly different phenomena, Hu used "
            "information about how ants move inside colonies to calculate how the particles of light that make "
            "up laser beams travel through snow.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) a collaboration", "B) an accessory", "C) a contradiction", "D) an analogy"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The text says Hu \"identif[ied] broad similarities between two seemingly "
            "different phenomena,\" comparing ants with light particles. An analogy seeks similarities between "
            "seemingly unrelated phenomena, fitting the context perfectly. "
            "Choice A is incorrect. \"A collaboration\" refers to working with others, but what follows describes "
            "a comparison between two phenomena, not collaboration. "
            "Choice B is incorrect. \"An accessory\" refers to something added to increase usefulness; no "
            "accessories are described. "
            "Choice C is incorrect. \"A contradiction\" means a set of opposed ideas; the text describes "
            "similarity, not difference."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "fb052096",
        "question_text": (
            "Part of the Atacama Desert in Peru has surprisingly rich plant life despite receiving almost no "
            "rainfall. Moisture from winter fog sustains plants once they're growing, but the soil's tough crust "
            "makes it hard for seeds to germinate in the first place. Local birds that dig nests in the ground "
            "seem to be of help: they churn the soil, exposing buried seeds to moisture and nutrients. Indeed, "
            "in 2016 Cristina Rengifo Faiffer found that mounds of soil dug up by birds were far more fertile "
            "and supported more seedlings than soil in undisturbed areas.\n\n"
            "Which choice best describes the function of the underlined portion in the text as a whole?"
        ),
        "choices": [
            "A) It elaborates on the idea that the top layer of Atacama Desert soil forms a tough crust.",
            "B) It describes the process by which seeds are deposited into Atacama Desert soil.",
            "C) It identifies the reason particular bird species dig nests in Atacama Desert soil.",
            "D) It explains how certain birds promote seed germination in Atacama Desert soil.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The underlined portion explains how local birds churn the soil, "
            "exposing buried seeds to moisture and nutrients—that is, how they promote seed germination. "
            "The last sentence provides further evidence supporting this explanation. "
            "Choice A is incorrect because the underlined portion doesn't address the soil's tough crust or "
            "its formation. "
            "Choice B is incorrect because the underlined portion describes how birds support seed germination "
            "but doesn't describe how seeds are deposited into the soil. "
            "Choice C is incorrect because neither the underlined portion nor the text identifies a reason that "
            "birds choose to dig ground nests."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "268c349d",
        "question_text": (
            "Text 1\nPhilosopher G.E. Moore's most influential work entails the concept of common sense. He "
            "asserts that there are certain beliefs that all people, including philosophers, know instinctively "
            "to be true, whether or not they profess otherwise: among them, that they have bodies, or that they "
            "exist in a world with other objects that have three dimensions. Moore's careful work on common "
            "sense may seem obvious but was in fact groundbreaking.\n\n"
            "Text 2\nExternal world skepticism is a philosophical stance supposing that we cannot be sure of "
            "the existence of anything outside our own minds. During a lecture, G.E. Moore once offered a proof "
            "refuting this stance by holding out his hands and saying, \"Here is one hand, and here is another.\" "
            "Many philosophers reflexively reject this proof (Annalisa Coliva called it \"an obviously annoying "
            "failure\") but have found it a challenge to articulate exactly why the proof fails.\n\n"
            "Based on the texts, how would the author of Text 1 most likely respond to proponents of the "
            "philosophical stance outlined in Text 2?"
        ),
        "choices": [
            "A) By agreeing with those proponents that Moore's treatment of positions that contradict his own is fundamentally unserious",
            "B) By suggesting that an instinctive distaste for Moore's position is preventing external world skeptics from constructing a sufficiently rigorous refutation of Moore",
            "C) By arguing that if it is valid to assert that some facts are true based on instinct, it is also valid to assert that some proofs are inadequate based on instinct",
            "D) By pointing out that Moore would assert that external world skepticism is at odds with other beliefs those proponents must unavoidably hold",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. According to the author of Text 1, Moore's common sense includes the "
            "belief that we all \"exist in a world with other objects.\" The author would observe that Moore would "
            "respond to external world skeptics by arguing that since everyone instinctively knows things exist "
            "outside their own minds, external world skepticism must be wrong. "
            "Choice A is incorrect because the author of Text 1 seems to agree with Moore, not that his treatment "
            "of opposing views is unserious. "
            "Choice B is incorrect because the author of Text 1 never mentions external world skeptics directly "
            "or why they have a hard time refuting Moore. "
            "Choice C is incorrect because Text 1's presentation of Moore's concept only includes the idea that "
            "some facts are true based on instinct—not that some proofs are inadequate based on instinct."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "318da9d3",
        "question_text": (
            "Domesticated thousands of years ago by Indigenous people in South America, cacao, the plant from "
            "which chocolate is made, deviates structurally from the wild plant it is descended from. Maize "
            "(corn), another crop domesticated by Indigenous Americans, shows so little resemblance to any wild "
            "plant that genetic research was necessary to ______ teosinte grass as its ancestor.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) acquire", "B) develop", "C) attract", "D) confirm"],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. \"Confirm\" means to establish the truth or correctness of something. "
            "Maize shows so little resemblance to any wild plant that scientific verification was required to "
            "establish teosinte grass as its ancestor with certainty. "
            "Choice A is incorrect because to \"acquire\" means to obtain possession; this doesn't fit. "
            "Choice B is incorrect because to \"develop\" means to create or promote growth; the ancestral "
            "relationship already existed—scientists didn't create it. "
            "Choice C is incorrect because to \"attract\" means to entice or bring about a relationship; the "
            "scientists verified the prior existence of the relationship, not brought it about."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "75edb37f",
        "question_text": (
            "Why do sand cats purr but lions roar? Researchers hypothesize that this difference between the two "
            "feline species may be partly due to a U-shaped bone in their throats called the hyoid. Sand cats, "
            "which are much smaller than lions, have a rigid hyoid that rumbles when the cat's larynx vibrates, "
            "resulting in a purr. By contrast, lions have a somewhat flexible hyoid, and the bone is attached "
            "to the skull with a stretchy ligament that sand cats lack. These traits allow lions and most other "
            "species of big cats to produce powerful roars. The same traits may also prevent most big cats from "
            "purring.\n\n"
            "Which choice best describes the overall structure of the text?"
        ),
        "choices": [
            "A) The text presents a theory about two species, then discusses facts that weaken it.",
            "B) The text compares the habitats of two species, then explains how those habitats are changing.",
            "C) The text describes a behavior shared by two species, then discusses other behaviors shared by them.",
            "D) The text poses a question about two species, then presents a possible answer.",
        ],
        "correct_answer": "D",
        "explanation": (
            "Choice D is the best answer. The text begins by posing a question: \"Why do sand cats purr but lions "
            "roar?\" The remainder presents a possible answer by explaining a hypothesis about differences in the "
            "hyoid bone structure—sand cats have rigid hyoids producing purring, while lions have flexible hyoids "
            "enabling roaring. "
            "Choice A is incorrect because the text asks a question and discusses a potential answer, not facts "
            "that weaken a theory. "
            "Choice B is incorrect because the text doesn't discuss habitats at all. "
            "Choice C is incorrect because the text focuses on different vocalization behaviors of each species, "
            "not a behavior they share."
        ),
        "domain": "Craft and Structure",
        "skill": "Text Structure and Purpose",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "b0e12b3a",
        "question_text": (
            "The work of molecular biophysicist Enrique M. De La Cruz is known for ______ traditional boundaries "
            "between academic disciplines. The university laboratory that De La Cruz runs includes engineers, "
            "biologists, chemists, and physicists, and the research the lab produces makes use of insights and "
            "techniques from all those fields.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) epitomizing", "B) transcending", "C) anticipating", "D) reinforcing"],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. \"Transcending\" means going beyond. \"Transcending traditional "
            "boundaries\" means crossing into all those various fields of research, which matches the description "
            "of the lab using insights and techniques from engineering, biology, chemistry, and physics. "
            "Choice A is incorrect. \"Epitomizing traditional boundaries\" would mean being a perfect example "
            "of keeping fields separate—the opposite of what we want. "
            "Choice C is incorrect. \"Anticipating\" means expecting or waiting for, resulting in a confusing "
            "sentence. "
            "Choice D is incorrect. \"Reinforcing traditional boundaries\" would mean keeping the fields separate—"
            "the opposite of what the text describes."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "63d61895",
        "question_text": (
            "During a 2014 archaeological dig in Spain, Vicente Lull and his team uncovered the skeleton of a "
            "woman from El Algar, an Early Bronze Age society, buried with valuable objects signaling a high "
            "position of power. This finding may persuade researchers who have argued that Bronze Age societies "
            "were ruled by men to ______ that women may have also held leadership roles.\n\n"
            "Which choice completes the text with the most logical and precise word or phrase?"
        ),
        "choices": ["A) waive", "B) concede", "C) refute", "D) require"],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. \"Concede\" means to admit something is true after first resisting that "
            "admission. The finding challenges the view that only men held power, and may persuade those "
            "researchers to admit that women may have also held leadership roles. "
            "Choice A is incorrect because \"waive\" means to refrain from insisting a right be observed; it "
            "isn't used when someone acknowledges an opinion may be invalid. "
            "Choice C is incorrect because \"refute\" means to demonstrate something is false; the finding "
            "supports the view that women held leadership roles, not that they didn't. "
            "Choice D is incorrect because in this context, \"require\" means to demand something as mandatory, "
            "which doesn't fit."
        ),
        "domain": "Craft and Structure",
        "skill": "Words in Context",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
    {
        "id": "d43f1594",
        "question_text": (
            "Text 1\nIn 2021, a team led by Amir Siraj hypothesized that the Chicxulub impactor—the object that "
            "struck the Yucatán Peninsula sixty-six million years ago, precipitating the mass extinction of the "
            "dinosaurs—was likely a member of the class of long-period comets. As evidence, Siraj cited the "
            "carbonaceous chondritic composition of samples from the Chicxulub impact crater as well as of "
            "samples obtained from long-period comet Wild 2 in 2006.\n\n"
            "Text 2\nAlthough long-period comets contain carbonaceous chondrites, asteroids are similarly rich "
            "in these materials. Furthermore, some asteroids are rich in iridium, as Natalia Artemieva points "
            "out, whereas long-period comets are not. Given the prevalence of iridium at the crater and, more "
            "broadly, in geological layers deposited worldwide following the impact, Artemieva argues that an "
            "asteroid is a more plausible candidate for the Chicxulub impactor.\n\n"
            "Based on the texts, how would Artemieva likely respond to Siraj's hypothesis, as presented in Text 1?"
        ),
        "choices": [
            "A) By insisting that it overestimates how representative Wild 2 is of long-period comets as a class",
            "B) By arguing that it does not account for the amount of iridium found in geological layers dating to the Chicxulub impact",
            "C) By praising it for connecting the composition of Chicxulub crater samples to the composition of certain asteroids",
            "D) By concurring that carbonaceous chondrites are prevalent in soil samples from sites distant from the Chicxulub crater",
        ],
        "correct_answer": "B",
        "explanation": (
            "Choice B is the best answer. Siraj hypothesizes the Chicxulub impactor was a long-period comet. "
            "But Artemieva points to iridium found in the crater and in \"geological layers that were deposited "
            "worldwide after the impact\" as evidence it was actually an asteroid, not a long-period comet. "
            "Choice A is incorrect because Text 2 never discusses whether Wild 2 is representative of long-period "
            "comets in general. "
            "Choice C is incorrect because Siraj's hypothesis connects the crater samples to comet Wild 2, not "
            "to asteroids. "
            "Choice D is incorrect because \"soil samples from sites distant from the Chicxulub crater\" is too "
            "vague—only samples connected to the impact are relevant."
        ),
        "domain": "Craft and Structure",
        "skill": "Cross-Text Connections",
        "difficulty": "Medium",
        "source": "EQB",
        "image_path": "",
    },
]


def main() -> None:
    output_path = Path("data/structured/craft_and_structure_medium.jsonl")

    print(f"Embedding {len(QUESTIONS)} questions…")
    embed_batch(QUESTIONS)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        for q in QUESTIONS:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")

    print(f"Wrote {len(QUESTIONS)} records → {output_path}")
    print("Next step: python -m ingestion.load data/structured/craft_and_structure_medium.jsonl")


if __name__ == "__main__":
    main()
