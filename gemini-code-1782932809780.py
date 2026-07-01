import streamlit as st
import pandas as pd
import io

# --- PAGE SETUP & STYLE ---
st.set_page_config(page_title="Preschool Content Hub", page_icon="🧸", layout="wide")

# Custom CSS injection for Pastel Montessori Brand Vibe
st.markdown("""
    <style>
    :root {
        --primary: #F4C95D;
        --secondary: #8DD3C7;
        --accent: #FF8E72;
    }
    .main .block-container { padding-top: 2rem; }
    h1 { color: #2C3E50; font-family: 'Poppins', sans-serif; }
    h2, h3 { color: #34495E; font-family: 'Poppins', sans-serif; }
    .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: bold; }
    </style>
""", unsafe_type=True)

st.title("🧸 Preschool Social Media Master Workspace")
st.markdown("Welcome to your agency-grade content management hub. Navigate through content pillars, preview copy formats, and export sheets to Excel instantly.")

# --- FULL PRODUCTION DATABASE ENGINE ---
@st.cache_data
def load_content_database():
    days_data = [
        # --- WEEK 1 ---
        {
            "Day": 1, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Campus Infrastructure", "Format": "Reel", "Title": "The Grand Tour", 
            "Visual_Layout_Script": "Hook (0-3s): Close-up of teacher opening a bright classroom door, smiling. On-screen text: 'What a 100x safer preschool space actually looks like...'\nSequence (0:03-0:15): Slow eye-level glide showing rounded wooden furniture, child-height sinks, soft reading nooks under bright morning sunlight.", 
            "Caption": "The Secret Language of Spaces 🧸✨\n\nChildren don’t just read books; they read rooms. They read the height of a shelf, the texture of a rug, and the sharpness of a corner. If a space is too rigid, their curiosity shrinks. If it's built with their scale and safety in mind, their imagination expands.\n\nWhen we designed [Preschool Name], we didn't just decorate walls—we built an ecosystem of exploration. Every piece of furniture features rounded edges, every shelf sits comfortably at eye level to foster independence, and our sensory play stations use non-toxic, sustainable materials. We believe that early childhood education isn't about sitting still at a desk; it's about moving safely through an environment designed to say 'Yes, you can touch that!'\n\nGiving your little one a secure launchpad to explore their world changes how they view learning for the rest of their lives.", 
            "CTA": "Drop a 'TOUR' in the comments below, and our team will send a DM to schedule your private walkthrough.", 
            "Hashtags": "#PreschoolTour #MontessoriEnvironment #EarlyChildhoodEducation #SafeSpacesForKids #PreschoolAdmissions #ChildLedLearning"
        },
        {
            "Day": 2, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Teacher Care", "Format": "Carousel", "Title": "Meet the Heart of Our School", 
            "Visual_Layout_Script": "Slide 1: Photo of teacher smiling warmly at eye level with a child. Text: 'Degrees matter. Empathy matters more.'\nSlide 2: Split screen showing classroom chaos vs calm guided interaction.\nSlide 3: Text breaking down ECCE qualifications and active listening methods.\nSlide 4: Close up of gentle emotional co-regulation in progress.\nSlide 5: Action CTA slide.", 
            "Caption": "Beyond the Lesson Plan: The Art of Early Mentorship 👩‍🏫❤️\n\nLet's be honest—anyone can hand a child a coloring sheet. But it takes a deeply intentional educator to notice the quiet child struggling to share, or the student who needs to run around for five minutes before they can focus on a puzzle.\n\nOur educators don't stand at the front of a classroom lecturing. You will almost always find them right down on the floor, at eye level, meeting our children exactly where they are. Backed by certified backgrounds in early childhood development, our team views every interaction—even a tantrum over a toy—as a vital learning moment for emotional regulation and social skills.\n\nWe don't just teach the alphabet; we nurture resilience, curiosity, and kindness.", 
            "CTA": "Leave a warm note for our incredible teachers in the comments below! What’s the number one quality you look for in your child's mentor?", 
            "Hashtags": "#PreschoolTeachers #EarlyChildhoodEducator #PositiveParenting #TeacherAppreciation #NurturingMinds #ActiveListeningKids"
        },
        {
            "Day": 3, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Daily Routines", "Format": "Reel", "Title": "A Day in the Life", 
            "Visual_Layout_Script": "Hook (0-3s): Child putting shoes neatly on a low cubby shelf. Text: 'What actually happens between drop-off and pick-up?'\nSequence (0:03-0:15): Fast, joyful cuts of morning circle time, hands pouring water at sensory tables, outdoor play on green lawns, and dim storytime transitions.", 
            "Caption": "What Does a Balanced Day Look Like For a 3-Year-Old? ☀️🧩\n\nFor a young child, predictability equals safety. When they know what comes next, their anxiety drops, and their willingness to take healthy learning risks shoots through the roof.\n\nAt [Preschool Name], our daily routine is mindfully structured around the natural rhythm of early childhood energy levels:\n\n👉 Morning Circle: Building social bonds, vocabulary, and tracking the weather.\n👉 Sensory & Cognitive Work: Hands-on math, language objects, and practical life skills.\n👉 Gross Motor Play: Outdoor time to move, run, and develop spatial awareness.\n👉 Reflective Storytime: Winding down the day with language-rich narratives.\n\nWe structure our days so your child returns home not just tired, but deeply fulfilled, inspired, and excited to return tomorrow.", 
            "CTA": "DM us 'ROUTINE' and we’ll send over our complete daily breakdown file directly to your inbox.", 
            "Hashtags": "#DayInTheLife #PreschoolRoutine #ToddlerSchedule #PlayBasedLearning #IndependentKids #EarlyYearsEducation"
        },
        {
            "Day": 4, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Introduction / Trust", "Format": "Static Image", "Title": "Why Our Welcome Routine Matters", 
            "Visual_Layout_Script": "Candid, high-quality photograph focusing on an educator offering a warm high-five to a child at the doorway while the parent smiles reassuringly in the background.", 
            "Caption": "Goodbye Tears? Here’s How We Handle Morning Transitions 🫂👋\n\nDrop-off times can be tough—both for the little feet stepping into the classroom and the parents walking back to their cars. Separation anxiety is a completely normal, beautiful sign of a strong bond.\n\nBecause we know this transition sets the tone for the entire day, we don't rush it. Our 'Welcome Routine' is gentle, individualized, and unhurried. Teachers meet each child with a personalized greeting—a high-five, a hug, or a quiet conversation about their favorite toy. We allow children to bring a comforting transition item from home if needed, and we guide them immediately into an engaging morning activity that redirects their focus naturally.\n\nRest assured, within minutes of you leaving, those tears almost always turn into curious smiles. We've got them, and we promise to treasure their hearts just as much as you do.", 
            "CTA": "Parents, what is your go-to morning drop-off routine or phrase that helps your child feel brave? Let’s share some wisdom below!", 
            "Hashtags": "#SeparationAnxiety #MorningRoutine #ParentingTips #PreschoolLife #GentleParenting #FirstDayOfSchoolFeelings"
        },
        {
            "Day": 5, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Campus & Philosophy", "Format": "Carousel", "Title": "The Montessori Practical Life Shelf", 
            "Visual_Layout_Script": "Slide 1: Child pouring water precisely from a tiny ceramic pitcher. Text: 'It looks like pouring water. It’s actually pre-writing.'\nSlide 2: Focus on pincer grip coordination mechanics.\nSlide 3: Visual detail explaining wrist muscle development.\nSlide 4: Showing execution paths for focus and order logic.\nSlide 5: Action curriculum CTA card.", 
            "Caption": "Why 'Ordinary' Tasks Build Extraordinary Brains 🧠✨\n\nIf you visit a traditional classroom, you might expect to see worksheets and flashcards. If you visit [Preschool Name], you're more likely to see a child meticulously transferring chickpeas between two bowls with a spoon, or polishing a small brass plate.\n\nTo an untrained eye, this looks like simple play. To an early childhood developmental specialist, this is the foundation of high-level cognitive growth. Dr. Maria Montessori observed that children have an innate desire to master the real-world movements they see adults do. Our Practical Life curriculum feeds this hunger. When a toddler practices pouring water without spilling, they are developing visual spatial awareness, hand-eye coordination, executive function, and an incredibly long attention span.\n\nWhen your child does things for themselves, they build an internal identity that says: 'I am capable. I am independent.'", 
            "CTA": "Want to bring these principles home? Drop a comment below, and we’ll send you our free guide: '5 Simple Ways to Set Up a Montessori-Inspired Space at Home.'", 
            "Hashtags": "#MontessoriCurriculum #PracticalLife #FineMotorSkills #IndependentToddler #CognitiveDevelopment #PreschoolActivities"
        },
        {
            "Day": 6, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Campus Security", "Format": "Reel", "Title": "Safety Beyond the Checklist", 
            "Visual_Layout_Script": "Hook (0-3s): Close-up of authorized smart access card tapping a security console. Text: 'The 3 safety barriers between the street and your child.'\nSequence (0:03-0:15): Quick tracking shots of guard gated entrance checkpoint, teacher sanitizing classroom materials, live administrative CCTV array views.", 
            "Caption": "Because Your Trust is Our Most Sacred Asset 🔐❤️\n\nWe know that choosing a preschool isn't just about the best books, the prettiest classrooms, or the most vibrant playgrounds. It comes down to one fundamental question: Will my child be safe?\n\nAt [Preschool Name], safety isn't an afterthought or a line on a marketing brochure. It is the framework around which every single school day is engineered.\n\nHere are our non-negotiables:\n🛡️ Controlled Access: Our campus features single-point entry protocols with verification required for every single visitor. No exceptions.\n🛡️ Sanitation Benchmarks: Every material, toy, and surface is deep-cleaned daily using non-toxic, eco-friendly agents safe for curious little mouths and hands.\n🛡️ Trained Eyes: 100% of our teaching and support staff are certified in pediatric First Aid and CPR, backed by robust background checks.\n\nWe protect your children with the same fierce attentiveness that you do at home.", 
            "CTA": "Have questions about our health policies or check-in apps? Send us a direct message—we practice complete transparency.", 
            "Hashtags": "#ChildSafetyFirst #SafePreschool #PreschoolSecurity #ParentPeaceOfMind #HealthyClassroom #EarlyYearsCare"
        },
        {
            "Day": 7, "Week": "Week 1", "Theme": "Welcome to Learning", "Pillar": "Community & Inclusion", "Format": "Static Image", "Title": "Weekly Reflection", 
            "Visual_Layout_Script": "Clean graphic text layout with soft borders on a muted pastel backdrop: 'It takes a village to raise a child, and an intentional school to anchor it.'", 
            "Caption": "It Takes a Village—Welcome to Ours 🌳✨\n\nAs we wrap up our first week of the month, we are reflecting deeply on the beautiful word Community.\n\nRaising a child in today's fast-paced world can sometimes feel incredibly isolating. Parents face endless conflicting advice online, busy work schedules, and the constant pressure to be perfect. But early childhood development was never meant to be a solo journey. It is meant to be shared.\n\nAt [Preschool Name], we don't just enroll children; we embrace whole families. We are here to celebrate the milestones, provide a listening ear during tough behavioral transitions, and build a warm space where parents can connect, share stories, and grow alongside one another.\n\nTo all our current and incoming families: Thank you for trusting us with your world. And to those still looking for their village—our doors are open, and there is a seat at the table waiting for you.", 
            "CTA": "Admissions close soon for this cohort. Send a DM to join our parent community today.", 
            "Hashtags": "#PreschoolCommunity #ParentSupport #ItTakesAVillage #ConsciousParenting #SchoolFamily #EarlyYearsMatter"
        },

        # --- WEEK 2 ---
        {
            "Day": 8, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Development & Activities", "Format": "Reel", "Title": "The Physics of Block Play", 
            "Visual_Layout_Script": "Hook (0-3s): Toddler adjusting a wobbly top block with absolute focus. Text: 'Your child isn’t just stacking blocks. They’re studying physics...'\nSequence (0:03-0:15): Macro focus tracking hands selecting architectural shapes, structural balancing, and the joyful smile when it inevitably tumbles down.", 
            "Caption": "The Secret Math Behind the Toy Box 🪵📐\n\nTo an adult, it looks like a pile of scattered wooden blocks on a rug. To a child's developing brain, it is a laboratory.\n\nLong before children encounter formal geometry or physics textbooks, they understand them intuitively through their hands. When your little one tries to balance a heavy triangular prism on top of a thin cylinder, they are calculating mass, gravity, and equilibrium.\n\nAt [Preschool Name], we deliberately prioritize open-ended materials like solid wooden blocks over flashing electronic toys. Electronic toys do the thinking for the child—press a button, get a flash of light. But a block demands everything from them. It forces them to plan, try, fail, regulate their frustration when the tower falls, and mathematically redesign their structure from the ground up.\n\nNext time you see your child building a tower, watch their eyes. You're watching a future architect, engineer, or scientist testing hypotheses in real-time.", 
            "CTA": "What is your child’s absolute favorite toy to build with at home right now? Let us know in the comments below!", 
            "Hashtags": "#PlayBasedLearning #StemForKids #EarlyEngineering #MontessoriToddler #CognitiveDevelopment #LearningThroughPlay"
        },
        {
            "Day": 9, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Fine Motor Development", "Format": "Carousel", "Title": "The Stages of Scissor Skills", 
            "Visual_Layout_Script": "Slide 1: Child-safe loop scissors slicing playdough seamlessly. Text: 'Why we don't start scissor practice with paper.'\nSlide 2: Visualizing the parent pain point of torn sheets and frustration.\nSlide 3: Breakdown of Stage 1 (Snipping thick resistive playdough logs).\nSlide 4: Breakdown of Stage 2 (Single cardstock fringe success cuts).\nSlide 5: Breakdown of Stage 3 (Continuous linear tracking tracking).\nSlide 6: Milestone sheet collection download CTA.", 
            "Caption": "The Anatomy of Learning to Cut ✂️🖐️\n\nUsing scissors seems simple to us, but for a 3-year-old, it requires a staggering amount of neurological and physical coordination. It demands bilateral coordination (using both hands differently at the same time), visual tracking, and the integration of the hand's tiny stabilizer muscles.\n\nIf you hand a child standard paper too soon, the paper flops, the blades twist, and the child feels defeated.\n\nThat’s why our educators introduce scissor skills through a highly intentional, phased framework. We start with playdough logs because the thick texture holds the blade straight. Then, we move to thick cardboard strips where a single squeeze yields a satisfying result. When we respect the natural timeline of physical development, children don't just learn a skill—they build deep, unshakeable confidence in their own capabilities.", 
            "CTA": "Comment 'SKILLS' below, and we'll DM you our step-by-step Fine Motor Activity Guide to try at home!", 
            "Hashtags": "#FineMotorSkills #ScissorSkills #EarlyYearsEducation #PreschoolActivities #MontessoriAtHome #ChildDevelopmentMilestones"
        },
        {
            "Day": 10, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Creativity & Sensory Play", "Format": "Reel", "Title": "Messy Play, Organized Brains", 
            "Visual_Layout_Script": "Hook (0-3s): Hands squishing vibrant cornstarch gloop into a dynamic swirl pattern. Text: 'Why messy clothes mean a highly active brain...'\nSequence (0:03-0:15): Eye-level views of sensory bin play, pouring oats with tiny cups, and playful cleanup steps with teachers.", 
            "Caption": "Praise the Mess! 🎨 Touch is intelligence. Long before abstract concepts occur, a child encounters the world via soft textures, temperature changes, and structural resistance.\n\nWe completely understand the instinct to want to keep our children's clothes pristine. But early childhood is an intensely tactile experience. Toddlers don't just learn by looking or listening; they learn by touching.\n\nWhen your child participates in sensory 'messy play' at [Preschool Name], their brain is working overtime. They are discovering descriptive vocabulary terms naturally ('sticky,' 'grainy,' 'heavy'), developing hand strength, and forming critical neural pathways that link cognitive concepts to physical sensations. Messy play is also an incredible tool for emotional regulation, providing deep tactile input that helps ground an overstimulated nervous system.", 
            "CTA": "Parents: Are you team 'Messy Play at Home' or team 'Leave it for the Preschool'? Let’s have an honest chat in the comments!", 
            "Hashtags": "#SensoryPlay #MessyPlay #SensoryBin #EarlyLearning #TactileLearning #LetThemBeLittle #PreschoolLife"
        },
        {
            "Day": 11, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Philosophy & Mindset", "Format": "Static Image", "Title": "The Secret Power of 'Boredom'", 
            "Visual_Layout_Script": "Aesthetic minimal crop showing a child sitting in soft lighting, turning a plain empty cardboard box over thoughtfully to explore its panels.", 
            "Caption": "\"Mom, I’m Bored!\" (And why that's a good thing) 🧸💭\n\nIn a world of instant digital entertainment, it is tempting to fill every single second of a child’s schedule with structured activities or screen time. The moment a child whines about boredom, we rush to solve it.\n\nBut at [Preschool Name], we view boredom as an essential educational milestone. When we intentionally step back and allow children to experience empty spaces in their day, something magical happens. Once the initial discomfort passes, their internal engine kicks in. A cardboard box suddenly becomes a spaceship. A pile of pillows transforms into a mountain range. Boredom is the exact incubator required to hatch authentic creative thinking, self-reliance, and deep imaginative play.\n\nOur classrooms are designed with independent choice periods where teachers step back into an observant role.", 
            "CTA": "The next time your little one says they have nothing to do, try smiling and saying, 'I can't wait to see what your brain invents today.'", 
            "Hashtags": "#UnstructuredPlay #CreativeKids #ImaginativePlay #ConsciousParenting #IndependentPlay #LetThemExplore"
        },
        {
            "Day": 12, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Early Numeracy", "Format": "Carousel", "Title": "Building Math Foundations Without Worksheets", 
            "Visual_Layout_Script": "Slide 1: Line of 5 miniature toy cars paired next to 5 counted buttons. Text: 'Why counting to 100 doesn't mean your child knows math.'\nSlide 2: Exposing the fallacy of rote verbal sequencing vs physical quantity mapping.\nSlide 3: Illustrating One-to-One Correspondence in daily life loops.\nSlide 4: Sorting natural items (shells, leaves) as geometric algebraic building blocks.\nSlide 5: Admissions tour curriculum alignment call to action.", 
            "Caption": "Rote Reciting vs. Deep Math Conceptions 🔢 master early mathematics. But real mathematical thinking runs much deeper than verbal memorization. True mathematical comprehension is spatial, tangible, and physical.\n\nIn our classrooms, you won’t find early learners filling out dry number tracking sheets. Instead, you will see them setting a child-sized dining table—counting out exactly four plates for four friends. You will see them categorizing button collections from largest to smallest, or weighing heavy rocks against light feathers on a balance scale.\n\nBy interacting with math physically, they learn what numbers mean, not just what they sound like. This concrete foundation ensures that when they encounter abstract fractions later, their brains can visualize reality.", 
            "CTA": "Experience a curriculum designed for true understanding. Book a school tour through the link in our bio.", 
            "Hashtags": "#EarlyMath #MathForToddlers #HandsOnLearning #MontessoriMath #LogicalThinking #EarlyChildhoodEducation"
        },
        {
            "Day": 13, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Gross Motor & Nature Play", "Format": "Reel", "Title": "The Outdoor Classroom Journey", 
            "Visual_Layout_Script": "Hook (0-3s): Dynamic low-angle shot of a child balancing on a natural log beam, arms extended. Text: 'The developmental skills hidden in outdoor play...'\nSequence (0:03-0:15): Running on uneven terrains, hanging from monkey bars, tracking insects under a large magnifying leaf tool.", 
            "Caption": "Why Strong Cores Build Strong Learners 🏃‍♂️🍃\n\nDid you know that a child's ability to sit still and focus at a desk in primary school depends heavily on the core strength they build during their preschool years?\n\nWhen children are given ample time to scale climbing frames, balance on logs, run over uneven lawns, and hang from bars, they develop their core abdominal muscles and vestibular system (the internal balance mechanism). Without a strong core, sitting upright becomes physically exhausting, causing children to fidget, lose focus, and tire out quickly later in their academic lives.\n\nOur outdoor play spaces aren't just for letting off steam between lessons. The outdoor space is a premium lesson plan. It challenges their bodies, invites calculated risk-taking, and connects them deeply to nature.", 
            "CTA": "Visit our link in bio to explore our extensive green campus facilities!", 
            "Hashtags": "#OutdoorClassroom #GrossMotorSkills #NaturePlay #ActiveKids #PreschoolPhysicalDevelopment #HealthyToddler"
        },
        {
            "Day": 14, "Week": "Week 2", "Theme": "Play is Learning", "Pillar": "Community & Reassurance", "Format": "Static Image", "Title": "The Value of Unedited Progress", 
            "Visual_Layout_Script": "Warm canvas graphic featuring soft natural tones and clean text overlay: 'Childhood is a beautiful journey, not a standardized race.'", 
            "Caption": "Learning is a Journey, Not a Race 🐢✨\n\nIt is incredibly easy to slip into the comparison trap. We look at other children and wonder: Why isn't my child writing their name yet? Why is that child talking in full paragraphs while mine still prefers non-verbal play?\n\nHere is our weekly reminder to take a deep, grounding breath: Childhood is not a competitive sport. Every child possesses their own internal, highly distinct developmental timeline. One child may focus entirely on mastering gross motor skills and climbing for three months, completely ignoring drawing. Another might sit quietly absorbing language for weeks before uttering a single sentence. Neither child is behind. Both are exactly where they need to be.\n\nAt [Preschool Name], we honor the individual rhythm of every single learner. Our job is to support them as they blossom beautifully at their own perfect pace.", 
            "CTA": "You are doing a wonderful job, parents. Trust your child's timeline.", 
            "Hashtags": "#TrustTheProcess #GentleParenting #ChildPacedLearning #PreschoolParenting #CelebrateIndividuality"
        },

        # --- WEEK 3 ---
        {
            "Day": 15, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Emotional Development", "Format": "Reel", "Title": "The Art of Co-Regulation", 
            "Visual_Layout_Script": "Hook (0-3s): Close-up of tearful child matching breathing rhythms with a kneeling educator. Text: 'Why we don't tell children to calm down...'\nSequence (0:03-0:15): Soft focus tracking of connection, holding space in a calm plush environment, and transition to shared coloring tasks.", 
            "Caption": "Borrowing Our Calm 🫂❤️\n\nA toddler's brain is like a highly sophisticated computer with an unfinished operating system. The prefrontal cortex—the area responsible for logic, reasoning, and self-control—is still under heavy construction.\n\nWhen a child throws a tantrum over a broken cracker or a transition to clean-up time, they aren't being manipulative. They are simply overwhelmed by an emotional wave they don't yet know how to navigate.\n\nAt [Preschool Name], you won't hear our educators say 'Stop crying' or 'It's not a big deal.' To a child, it is a big deal. Instead, we practice Co-Regulation. We kneel down, sit with them in their discomfort, validate their feelings ('It's hard to stop playing, I hear you'), and provide a steady, calm presence. Over time, this safe containment teaches the child's brain how to self-regulate.", 
            "CTA": "What is your favorite phrase to use when helping your child navigate a big boundary or emotional moment? Share it with our community below!", 
            "Hashtags": "#CoRegulation #EmotionalIntelligence #GentleParentingTips #ToddlerMeltdown #ConsciousParenting #PreschoolLife"
        },
        {
            "Day": 16, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Parent Partnership", "Format": "Carousel", "Title": "Shifting from 'How Was Your Day?'", 
            "Visual_Layout_Script": "Slide 1: Illustration of a parent asking questions to a shrugging kid. Text: 'Why your child answers Fine or Nothing at pickup.'\nSlide 2: Breaking down the cognitive wall of broad abstract query filters.\nSlide 3: Shift 1 (Sensory details: What made you laugh out loud today?)\nSlide 4: Shift 2 (Social loops: Who did you sit next to at snack?)\nSlide 5: Shift 3 (Rose & Thorn emotional checkin strategy chart).\nSlide 6: Visual fridge checklist printable code download CTA card.", 
            "Caption": "Cracking the Preschool Conversation Code 🗣️🧩\n\nYou buckle them into the car seat, look back with a warm smile, and ask the classic question: What did you do today? The inevitable response? Nothing. or I forgot.\n\nIt can be frustrating as a parent, but here is the developmental secret: young children live entirely in the present moment. Once a school day is over, it becomes a blur of past events. Compounding this, broad open-ended questions require high-level cognitive scanning that a tired toddler brain simply doesn't have the energy for after a busy day of learning.\n\nIf you want to unlock the details of their day, you need to provide specific, sensory, and emotional hooks. By narrowing the scope of your questions, you help them pinpoint a single memory file. Give these alternative prompts a shot tonight!", 
            "CTA": "Want a print-out list for your fridge? DM us 'TALK' and we'll send you our cheat sheet of 20 Creative Questions to Ask Instead of 'How Was Your Day?'", 
            "Hashtags": "#ParentChildConnection #ToddlerCommunication #ParentingHacks #PreschoolerLife #ActiveListening #FamilyTime"
        },
        {
            "Day": 17, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Socialization", "Format": "Reel", "Title": "Friendship Engineering", 
            "Visual_Layout_Script": "Hook (0-3s): Two children cooperatively locking a massive floor block unit. Text: 'How 3-year-olds actually learn to make friends...'\nSequence (0:03-0:15): Sharing tools down cross-tables, tracking a small peer problem solving session with a mentor, and afternoon dismissal waves.", 
            "Caption": "The Blueprint for Lifelong Social Success 🤝🌱\n\nSharing doesn't come naturally to a young child—and that is completely developmentally appropriate. In their early years, their worldview is centered entirely around their own needs and immediate space. True empathy and collaboration are skills that must be modeled, practiced, and gently integrated day after day.\n\nAt [Preschool Name], we view the classroom as a micro-society. We don't just stand back and hope the children sort it out. We intentionally build opportunities for social expansion:\n\n🚀 Collaborative Engineering: Projects designed so that two or three children must cooperate to achieve a goal.\n🚀 Assertiveness Training: Teaching children to hold out a firm hand and confidently say, 'I am using this right now.'\n🚀 Empathy Modeling: Guiding children to read body language and react with care.", 
            "CTA": "Tap the link in our bio to see how our social curriculum prepares your child for life!", 
            "Hashtags": "#SocialSkillsForKids #PreschoolFriendships #EarlyYearsLearning #ConflictResolutionKids #EmpathyInEducation #PositiveDiscipline"
        },
        {
            "Day": 18, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Classroom Culture", "Format": "Static Image", "Title": "The Circle Time Ritual", 
            "Visual_Layout_Script": "High angle structural focus photograph capturing early learners sat in a clean geometric ring outline on a textured rug space.", 
            "Caption": "Where Every Voice Has a Home ⭕✨\n\nEvery day at [Preschool Name] begins and ends in exactly the same way: on the rug, sitting in a perfect circle.\n\nTo a child, the circle holds profound psychological value. In a circle, there is no front, no back, and no hierarchy. Every single child can look directly into the eyes of every peer and teacher. It is our daily ritual of radical belonging. During our circle time, we don't just check the calendar or sing the weather song. We check in with one another's hearts. We pass around our community basket, giving each child an uninterrupted moment to share a thought, a dream, or even a worry.\n\nThis simple ritual grounds the morning, transitions their minds into a collaborative learning state, and subtly reinforces the message: You are seen. You are heard. You matter to this group.", 
            "CTA": "Want to experience the warmth of our school culture firsthand? Admissions are open for the upcoming term. Drop us a DM to secure a personal preview slot.", 
            "Hashtags": "#CircleTime #ClassroomRituals #SchoolCommunity #BelongingMatters #SocialEmotionalLearning #EarlyChildhoodEducation"
        },
        {
            "Day": 19, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Behavioral Guidance", "Format": "Carousel", "Title": "Setting Boundaries with Love at Home", 
            "Visual_Layout_Script": "Slide 1: Graphic comparing reactive vocalizing vs clear objective boundary holding. Text: 'Why Don't do that! rarely works.'\nSlide 2: Unpacking the visual command layer architecture of the toddler brain.\nSlide 3: Shift 1 (Switching prohibitive running cues to walking alignment actions).\nSlide 4: Shift 2 (Redirecting window hitting energies to soft pillow pads).\nSlide 5: Shift 3 (Replacing vague commands with clear optional outfit layouts).\nSlide 6: Behavioral guidance tracking follow CTA card.", 
            "Caption": "Speaking in the Affirmative: Changing How Your Child Listens 🔊❤️\n\nHave you ever felt like you're repeating yourself a hundred times a day, only to be met with blank stares or deliberate defiance? You are definitely not alone.\n\nOften, the breakdown isn't a lack of willingness from your child; it's a breakdown in linguistic translation. Because early learners are highly visual thinkers, their brains struggle to process negative commands efficiently. If you say 'Don't spill the milk,' their brain focuses entirely on the image of spilling milk.\n\nAt [Preschool Name], our educators utilize affirmative behavioral framing. We state the desired positive behavior immediately, clearly, and without anger. Instead of commanding them to stop a negative behavior, we paint a clear verbal picture of what success looks like.", 
            "CTA": "Save this post so you can easily reference these verbal shifts during high-stress moments!", 
            "Hashtags": "#PositiveBehaviorSupport #ParentingTips #GentleParentingLanguage #ToddlerBehavior #CommunicationSkills #MindfulParenting"
        },
        {
            "Day": 20, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Natural STEM", "Format": "Reel", "Title": "The Outdoor Loose Parts Laboratory", 
            "Visual_Layout_Script": "Hook (0-3s): Child building a bridge path out of raw logs and textured timber. Text: 'Why our playground doesn't have bright plastic swings...'\nSequence (0:03-0:15): Fluid channel alignment, stacking wooden pallets safely, and tracking clear water flows through custom conduits.", 
            "Caption": "The Genius of Loose Parts Play 🪵💧\n\nIf you give a child a plastic toy smartphone, they can only play with it in a handful of pre-programmed ways. But if you give a child a collection of bamboo pipes, wooden crates, and smooth river rocks, the possibilities are infinite. This is what early childhood specialists call Loose Parts Play.\n\nIn our premium outdoor learning spaces, we purposefully move away from static, single-use play equipment. Instead, we provide safe, natural materials that can be moved, stacked, combined, redesigned, and taken apart. When children interact with loose parts, they are entering a deep cognitive state of scientific inquiry. They ask themselves: How heavy is this log? How many rocks do I need to dam this water flow? They are mastering physical laws and learning spatial mathematics.", 
            "CTA": "Want to see the loose parts philosophy in action? Book a direct campus tour via the link in our bio!", 
            "Hashtags": "#LoosePartsPlay #StemOutdoors #NaturalPlaygrounds #ReggioEmiliaInspired #CriticalThinkingKids #PreschoolCurriculum"
        },
        {
            "Day": 21, "Week": "Week 3", "Theme": "Growing Together", "Pillar": "Family Trust", "Format": "Static Image", "Title": "Weekly Reflection", 
            "Visual_Layout_Script": "Warm soft candid photo capturing the mutual smile of an educator and parent handing over a child’s craft binder file at dismissal.", 
            "Caption": "Partners in Your Child's Wonder 🤍✨\n\nAs we bring this week to a close, we find ourselves reflecting on the immense privilege it is to walk alongside you on this parenting journey. We know that handing your little one over to a preschool isn't just an educational transaction. It is an act of deep, vulnerable trust. You are entrusting us with your absolute world—their laughter, their sensitive hearts, their growing minds, and their safety.\n\nPlease know that we never take that trust for granted. We don't see ourselves as just a school, but as an extension of your home. When we share their tiny developmental breakthroughs, guide them through social hurdles, or hold them through morning drop-off tears, we do it with the same love, intentionality, and respect that you practice daily.\n\nThank you for allowing us to be part of your village.", 
            "CTA": "Have a wonderful, restful weekend filled with memory-making, parents!", 
            "Hashtags": "#PreschoolFamily #ParentPartnership #ItTakesAVillage #EarlyYearsMatter #GratefulHearts #SchoolCommunity"
        },

        # --- WEEK 4 ---
        {
            "Day": 22, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Value Proposition", "Format": "Reel", "Title": "The True Return on Investment", 
            "Visual_Layout_Script": "Hook (0-3s): Confident early learner leading a clean line transition track. Text: 'What are you actually paying for in a premium preschool?'\nSequence (0:03-0:15): Educator mapping observations in a portfolio book, child sorting fine imports, warm executive desk interactions.", 
            "Caption": "Investing in the First 2000 Days 📊✨\n\nEconomists and neuroscientists agree on one striking fact: the highest economic and developmental return on education investment happens before a child ever steps into a primary school classroom. In fact, 90% of human brain development is structurally complete by age 5.\n\nWhen parents evaluate preschools, it is easy to look at tuition as a monthly expense. But at [Preschool Name], we invite you to view it as a foundational investment. Our premium structures ensure your child receives:\n\n💎 1:8 Educator Ratios: No child's unique emotional or cognitive rhythm is lost.\n💎 Scientifically Engineered Environments: Every material is physical, purposeful, and imported.\n💎 ECCE Certified Specialists: Our mentors are career educators trained in child psychology.", 
            "CTA": "Admissions close shortly for this cohort. Send us a DM with the word 'INVEST' to review our enrollment packages.", 
            "Hashtags": "#PreschoolAdmissions #EarlyEducationInvestment #ReturnOnEducation #PremiumPreschool #ChildDevelopment #ParentingDecisions"
        },
        {
            "Day": 23, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Logistics Clearance", "Format": "Carousel", "Title": "Your Top 5 Admissions FAQs Answered", 
            "Visual_Layout_Script": "Slide 1: Clean bold card layout design. Text: 'Thinking of enrolling? Let’s answer your top 5 questions honestly.'\nSlide 2: FAQ 1 details (Potty training partnerships and transition support workflows).\nSlide 3: FAQ 2 details (Strict 1:8 ratio layouts for emotional safety spaces).\nSlide 4: FAQ 3 details (Symptom-free safety isolation and deep cleaning benchmarks).\nSlide 5: FAQ 4 & 5 details (Organic meal updates and midterm structural entries).\nSlide 6: Direct onboarding link portal conversion CTA card.", 
            "Caption": "Transparency First: No Guesswork for Your Family 📝🔍\n\nChoosing the perfect preschool can feel overwhelming, especially when trying to gather clear logistics across different websites. We believe that a true partnership with parents begins with radical, upfront clarity.\n\nToday, we are opening up our notebook to answer the five questions that drop into our admissions inbox most frequently. Whether you are anxious about your child's eating habits, bathroom independence, or how they will adapt to a new schedule mid-term—we want you to breathe easy. Our school ecosystem is intentionally built to adapt to families, not force families into a rigid, unforgiving box.", 
            "CTA": "Have a question we missed? Drop it in the comments below, or send us a quick DM. Our Admissions Director answers every query personally!", 
            "Hashtags": "#PreschoolFAQ #PreschoolEnrollment #ParentingLogistics #TransparentEducation #SchoolAdmissions #ToddlerParents"
        },
        {
            "Day": 24, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Testimonials", "Format": "Reel", "Title": "From Tears to Triumphs", 
            "Visual_Layout_Script": "Hook (0-3s): Deep warm hug at afternoon dismissal lines. Text: 'What a real mom says about the first 30 days here...'\nSequence (0:03-0:15): Macro glide across handwritten testimonial cards, candid tracking clips of the child laughing, direct video interview snippets.", 
            "Caption": "A Letter from the Village 💌🥺\n\n'Before enrolling Aarav at [Preschool Name], my anxiety was through the roof. He had never been away from me for more than an hour. On the first morning, he clung to my leg and wept. I sat in my car and cried too, convinced I was making a mistake. But his teacher didn't rush him. She knelt down, validated his fear, and safely guided him in. By afternoon pick-up, he was showing me a sensory plate he made. Within a month, our mornings completely shifted...'\n\nWe share this because we know how heavy that walk back to your car can feel on day one. Separation anxiety is real, normal, and valid—for both of you. But with the right, gentle transition framework, those tears transform into confident independence.", 
            "CTA": "Spaces for our upcoming cohort are officially filling up. Tap the link in our bio to begin your application journey.", 
            "Hashtags": "#PreschoolTestimonial #ParentReview #SeparationAnxietySuccess #HappyParents #PreschoolCommunity #AdmissionsOpen"
        },
        {
            "Day": 25, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Academic Readiness", "Format": "Static Image", "Title": "A Peek Inside the Literacy Vault", 
            "Visual_Layout_Script": "Beautiful wide angle image displaying front-facing cover art books displayed symmetrically on reachable low wooden bookshelves.", 
            "Caption": "Nurturing a Lifelong Love for Words 📚🐛\n\nWe do not force young children to memorize sight words or sit through boring phonic drills. Why? Because flashcards teach children to decode symbols under pressure, but they rarely teach them to love reading.\n\nWelcome to our Literacy Vault—the quiet heart of our library space. Every book on these forward-facing shelves is chosen with meticulous curation. We feature diverse narratives, rich phonological vocabulary textures, and beautifully illustrated pages that spark deep curiosity. By placing books cover-out at a child's natural eye level, we encourage them to independently choose reading as a joyful activity. Our educators read aloud daily, transforming phonics into an immersive experience.", 
            "CTA": "Click our bio link to schedule a walk-through of our library and campus spaces.", 
            "Hashtags": "#EarlyLiteracy #PreschoolLibrary #PhonicsFun #RaiseAReader #LoveForBooks #PreschoolCurriculum"
        },
        {
            "Day": 26, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Safety Infrastructure", "Format": "Carousel", "Title": "The Security Protocol Deep Dive", 
            "Visual_Layout_Script": "Slide 1: Shield emblem template graphic card. Text: 'Our 4-Layer Safety Protocol: What keeps our campus completely secure.'\nSlide 2: Layer 1 mechanics (Biometric secure access control lobby frameworks).\nSlide 3: Layer 2 mechanics (Continuous live recorded multi angle CCTV feeds).\nSlide 4: Layer 3 mechanics (Childproof architectural profiling and rounded edge sets).\nSlide 5: Layer 4 mechanics (100% CPR/First Aid certification profiles and isolation bays).\nSlide 6: Physical security audit tour layout verification CTA.", 
            "Caption": "Uncompromising Safety, Complete Peace of Mind 🛡️🔒\n\nWhen you choose a preschool, you are entrusting that facility with your most precious asset. We do not take that lightly. Safety cannot simply be a checklist on a clipboard; it must be an structural component woven into the architecture of the daily schedule.\n\nFrom our single-point biometric entry gates to our meticulously planned medical-grade daily toy sanitation cycles, we have built an ecosystem designed to protect your child completely while preserving their freedom to move and explore. We have built a sanctuary where kids can simply be kids, and where parents can work through their day without a single moment of worry.", 
            "CTA": "Verify our certifications in person. Schedule a private weekday campus audit tour via the link in our bio.", 
            "Hashtags": "#PreschoolSafety #SecureCampus #ChildSafetyProtocols #SafeLearningEnvironment #ParentPeaceOfMind #PreschoolAdmissions"
        },
        {
            "Day": 27, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Onboarding Process", "Format": "Reel", "Title": "The 3-Step Enrollment Journey", 
            "Visual_Layout_Script": "Hook (0-3s): Sliding a clean embossed registration pack into a branded leatherette folder. Text: 'From booking a tour to your child’s first day: The 3 easy steps.'\nSequence (0:03-0:15): UI smartphone navigation paths, parent walkthrough smiles, unboxing a custom welcome kit box bundle.", 
            "Caption": "Your Clear Path to Joining Our Village 🗺️🎒\n\nWe know that parent schedules are packed. The last thing you need is a mountain of complex, confusing paperwork just to secure your child’s early education path. That’s why we’ve completely re-engineered our onboarding structure to be entirely smooth, modern, and high-support. You can complete the entire intake framework right from your phone or desktop:\n\n🗓️ Step 1: The Discovery Tour\n🗓️ Step 2: The Digital Application\n🗓️ Step 3: The Welcome Transition\n\nEnrollment allocations for the upcoming term are officially closing down. Let’s take the first step together today.", 
            "CTA": "Click the link in our bio to lock in your private campus preview date!", 
            "Hashtags": "#PreschoolEnrollment #HowToApply #AdmissionsOpen #ParentSupport #JoinOurSchool #ToddlerEducation"
        },
        {
            "Day": 28, "Week": "Week 4", "Theme": "Ready for Admissions", "Pillar": "Scarcity & Conversion", "Format": "Static Image", "Title": "Closing the Doors on This Cohort", 
            "Visual_Layout_Script": "Bold clean high-contrast card interface layout: 'Admissions Portal Closing Window. Strict 1:8 Mentorship Caps Applied.'", 
            "Caption": "Final Call: Seats are Officially Closing ⏳🎒\n\nWe have reached that point in our seasonal cycle where our classroom cohorts are almost perfectly balanced. To protect our strict 1:8 student-to-teacher ratios and ensure every single child receives deep, personalized mentorship, we have a hard cap on our enrollment allocations. This week represents our final call for applications for the current academic entry window.\n\nIf you have been scrolling through our feed and visualizing your little one exploring our practical life shelves—this is your moment to take action. Once these final remaining seats are filled, our enrollment portal will transition to a waitlist format until the next semester block.", 
            "CTA": "Click the link in our bio to submit your application or secure your emergency tour slot instantly before the doors close!", 
            "Hashtags": "#FinalCall #EnrollmentDeadline #PreschoolAdmissionsClosing #SecureYourSpot #EarlyYearsDevelopment #JoinUsNow"
        }
    ]
    return pd.DataFrame(days_data)

df = load_content_database()

# --- INSTANT EXCEL EXPORT ENGINE ---
def convert_df_to_excel(dataframe):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        dataframe.to_excel(writer, index=False, sheet_name='Master Data Table')
        for week_name in dataframe['Week'].unique():
            week_df = dataframe[dataframe['Week'] == week_name]
            week_df.to_excel(writer, index=False, sheet_name=week_name)
    return output.getvalue()

excel_data = convert_df_to_excel(df)

# --- SIDEBAR INTERACTIVE FILTERS ---
st.sidebar.header("🎯 Filter Workspace")
format_filter = st.sidebar.multiselect("Select Content Formats:", options=df["Format"].unique(), default=df["Format"].unique())
pillar_search = st.sidebar.text_input("Search Strategy Pillars:")

filtered_df = df[df["Format"].isin(format_filter)]
if pillar_search:
    filtered_df = filtered_df[filtered_df["Pillar"].str.contains(pillar_search, case=False) | filtered_df["Title"].str.contains(pillar_search, case=False)]

# --- EXCEL DOWNLOAD BUTTON ---
st.sidebar.markdown("---")
st.sidebar.subheader("📥 Master Export")
st.sidebar.download_button(
    label="Download Master Workbook (.xlsx)",
    data=excel_data,
    file_name="Preschool_Social_Media_Kit_July.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    use_container_width=True
)

# --- MASTER VIEWS TAB INTERFACE ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗓️ Full Data Grid", "🌸 Week 1", "🪵 Week 2", "🫂 Week 3", "📊 Week 4"])

with tab1:
    st.subheader("Complete Production View Matrix")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

def render_week_tab(week_label):
    week_data = filtered_df[filtered_df["Week"] == week_label]
    if week_data.empty:
        st.info("No matching posts found for the current filter settings.")
        return
        
    for idx, row in week_data.iterrows():
        with st.expander(f"📍 Day {row['Day']} | {row['Format']} — {row['Title']} ({row['Pillar']})"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**Theme Loop:** `{row['Theme']}`")
                st.markdown(f"**Format Anchor:** `{row['Format']}`")
                st.markdown("**🎬 Visual / Layout / Script:**")
                st.write(row['Visual_Layout_Script'])
                st.info(f"💡 **Call to Action Strategy:**\n\n{row['CTA']}")
            with col2:
                st.markdown("**📝 Premium Copy Deck:**")
                st.code(row['Caption'], language="text")
                st.caption(f"🏷️ **Hashtags:** {row['Hashtags']}")

with tab2: st.subheader("Theme: Welcome to Learning"); render_week_tab("Week 1")
with tab3: st.subheader("Theme: Play is Learning"); render_week_tab("Week 2")
with tab4: st.subheader("Theme: Growing Together"); render_week_tab("Week 3")
with tab5: st.subheader("Theme: Ready for Admissions"); render_week_tab("Week 4")