import React, { useEffect, useState } from 'react'
import NowNode from './components/Nodes/NowNode'
import PrevNextNodes from './components/Nodes/PrevNextNodes'

function App() {
    //const [nodesCount, setNodesCount] = useState()
	const [prevNodes, setPrevNodes] = useState(undefined)
	const [nowNode,   setNowNode]   = useState(undefined)
	const [nextNodes, setNextNodes] = useState(undefined)

	
	const getPrevNext = (id) => {
		fetch("/get_prev_next/" + id).then(responce => {
			if (responce.ok){
				return responce.json()
            }
        }).then(data => {
			if (typeof data === 'undefined') {
				console.log("Bad get responce")
            }
            else {
				setPrevNodes(data.nodes.Prev)
				setNowNode(data.nodes.Now)
				setNextNodes(data.nodes.Next)
            }
        })
    }

    useEffect(() => {
        getPrevNext(42)
    }, [])

	const handleNodeChange = (id) => {
		getPrevNext(id)
	}

	return (
		<div className="App">
			<div className="container-liquid">
				<div className="row">
					<PrevNextNodes nodes={prevNodes} onNodeChange={handleNodeChange} />
					<NowNode node={nowNode} />
					<PrevNextNodes nodes={nextNodes} onNodeChange={handleNodeChange} />
				</div>
			</div>
		</div>
	);
}

export default App;
