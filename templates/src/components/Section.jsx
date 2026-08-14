import ApiCard from './APICard'

export default function Section(){
    return(
        <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 mx-10">
            <ApiCard />
            <ApiCard />
        </section>
    )
}