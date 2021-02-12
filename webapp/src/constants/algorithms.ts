interface algorithm_props {
    name: String
    short_name: String
    type: String
}

export const algorithms : {[key: string]: algorithm_props}= {
    greedy: {
        name: "Greedy (González 1985)",
        short_name: "Greedy",
        type: "approximation"
    },
    greedy_reduce: {
        name: "Greedy (modified to optimise radii)",
        short_name: "Greedy Reduce",
        type: "approximation"
    },
    colourful_bandyapadhyay_pseudo: {
        name: "O(1)-colourful (Pseudo 2-approximation, Bandyapadhyay et al. 2019)",
        short_name: "Pseudo O(1)-colourful",
        type: "approximation"
    },
    colourful_bandyapadhyay: {
        name: "O(1)-colourful (17-approximation, Bandyapadhyay et al. 2019)",
        short_name: "O(1)-colourful",
        type: "approximation"
    },
    pbs: {
        name: "PBS (Pullan 2008)",
        short_name: "PBS",
        type: "genetic"
    },
    colourful_pbs: {
        name: "Colourful PBS",
        short_name: "Colourful PBS",
        type: "genetic"
    },
    brute_force_k_center: {
        name: "Brute force K-Center",
        short_name: "Brute force K-Center",
        type: "exact"
    },
    brute_force_colourful_k_center: {
        name: "Brute force Colourful K-Center",
        short_name: "Brute force Colourful K-Center",
        type: "exact"
    }
}