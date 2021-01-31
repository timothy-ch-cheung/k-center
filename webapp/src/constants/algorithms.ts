interface algorithm_props {
    name: String
    short_name: String
}

export const algorithms : {[key: string]: algorithm_props}= {
    greedy: {
        name: "Greedy (González 1985)",
        short_name: "Greedy"
    },
    greedy_reduce: {
        name: "Greedy (modified to optimise radii)",
        short_name: "Greedy Reduce"
    },
    colourful_bandyapadhyay_pseudo: {
        name: "O(1)-colourful (Pseudo 2-approximation, Bandyapadhyay et al. 2019)",
        short_name: "Pseudo O(1)-colourful"
    },
    colourful_bandyapadhyay: {
        name: "O(1)-colourful (17-approximation, Bandyapadhyay et al. 2019)",
        short_name: "O(1)-colourful"
    },
    pbs: {
        name: "PBS (Pullan 2008)",
        short_name: "PBS"
    },
    colourful_pbs: {
        name: "Colourful PBS",
        short_name: "Colourful PBS"
    }
}