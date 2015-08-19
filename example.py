#!/usr/bin/python
# -*- coding: utf-8 -*-

from nlps import nlps

# James Zammit
title = "Steve Jobs Biography"
text = "Steven Paul Jobs was born on February 24, 1955, in San Francisco, California, to Joanne Schieble (later Joanne Simpson) and Abdulfattah 'John' Jandali, two University of Wisconsin graduate students who gave their unnamed son up for adoption. His father, Abdulfattah Jandali, was a Syrian political science professor, and his mother, Joanne Schieble, worked as a speech therapist. Shortly after Steve was placed for adoption, his biological parents married and had another child, Mona Simpson. It was not until Jobs was 27 that he was able to uncover information on his biological parents. As an infant, Steven was adopted by Clara and Paul Jobs and named Steven Paul Jobs. Clara worked as an accountant, and Paul was a Coast Guard veteran and machinist. The family lived in Mountain View, California, within the area that would later become known as  Silicon Valley. As a boy, Jobs and his father would work on electronics in the family garage. Paul would show his son how to take apart and reconstruct electronics, a hobby that instilled confidence, tenacity and mechanical prowess in young Jobs. While Jobs was always an intelligent and innovative thinker, his youth was riddled with frustrations over formal schooling. Jobs was a prankster in elementary school, and his fourth-grade teacher needed to bribe him to study. Jobs tested so well, however, that administrators wanted to skip him ahead to high school—a proposal that his parents declined. A few years later, while Jobs was enrolled at Homestead High School (1971), he was introduced to his future partner, Steve Wozniak, through a friend of Wozniak's. Wozniak was attending the University of California, Berkeley, at the time. In a 2007 interview with PC World, Wozniak spoke about why he and Jobs clicked so well: 'We both loved electronics and the way we used to hook up digital chips,' Wozniak said. 'Very few people, especially back then, had any idea what chips were, how they worked and what they could do. I had designed many computers, so I was way ahead of him in electronics and computer design, but we still had common interests. We both had pretty much sort of an independent attitude about things in the world. ...'"

tt = nlps()

sentences = tt.summarize(title, text)

for sentence in sentences:
  print sentence