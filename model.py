import pandas as pd

# Load and prepare dataset
df = pd.read_csv("data_analyst_jobs_cleaned.csv")  # Put this CSV in your backend folder

# Clean skills
df['Skill'] = df['Skill'].fillna('')
df['Skill_List'] = df['Skill'].apply(lambda x: [skill.strip().lower() for skill in x.split(',')])
df['Education_Level'] = "Bachelor's"  # Add default education level

# Recommendation function
def recommend_jobs(user_skills, top_n=5):
    user_skills = [skill.strip().lower() for skill in user_skills.split(',')]
    recommendations = []

    for _, row in df.iterrows():
        job_skills = row['Skill_List']
        match_count = len(set(user_skills) & set(job_skills))
        if match_count > 0:
            recommendations.append({
                'Job Title': row['Job Title'],
                'Matched Skills': list(set(user_skills) & set(job_skills)),
                'Match Count': match_count,
                'Avg Salary': row['Avg_Salary'],
                'Education': row['Education_Level']
            })

    recommendations = sorted(recommendations, key=lambda x: (x['Match Count'], x['Avg Salary']), reverse=True)
    return recommendations[:top_n]
